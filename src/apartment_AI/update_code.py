#%% 업데이트 준비
#1. 라이브러리 불러오기
import pandas as pd
import requests
import json
import time
import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import numpy as np
from user_agent import generate_user_agent, generate_navigator
from urllib.error import HTTPError
import warnings
import ray
import os
import pymysql
from bs4 import BeautifulSoup
import re

warnings.filterwarnings(action = "ignore")

#2. ray 사용 준비
#(1). 코어 개수 확인
cores = os.cpu_count()
print(cores)

#(2). ray환경 열기
ray.shutdown()
ray.init()

#%% DB 연결 및 범위 지정
#2. 검색정보 불러오기
#(1). mysql의 infor DB에 접속
con = pymysql.connect(host = "localhost", user = "root", password="0000", db = "infor", charset='utf8')
cur = con.cursor()

#(2). 검색일자
query = """
    SELECT * FROM date
"""
cur.execute(query)
startDate = cur.fetchone()
startDate = 20200101

now = time.localtime()
endDate = time.strftime('%Y%m%d', now)

#(3). 검색대상
query = """
    SELECT * FROM TARGET
"""
examples = pd.read_sql_query(query, con)

#(4). 키값 받아오기
query = """
    SELECT * FROM KEY_VALUE
"""
key_list = pd.read_sql_query(query, con)
key1 = key_list.iloc[0,0]
key2 = key_list.iloc[0,1]
key3 = key_list.iloc[0,2]

#(5). 필요변수명
need = "area bjdongCd bldNm etcPurps exposPubuseGbCd exposPubuseGbCdNm flrGbCdNm mainAtchGbCd mainAtchGbCdNm mainPurpsCd mainPurpsCdNm mgmBldrgstPk newPlatPlc platPlc sigunguCd"
need = need.split()

con.close()

#%%검색대상의 배치화
#(1). 코어 수 확인하기
use_cores = os.cpu_count()
print(use_cores)

total = examples.shape[0]
batchsize = total / use_cores
batchsize = round(batchsize)
print(batchsize)

#(2). 배치화
batches = []
batches.append(examples[0:batchsize])

batches[0].shape

for i in range(1,use_cores) :
    batch_now = pd.concat(batches)
    
    if examples.shape[0] - batch_now.shape[0] > batchsize :
        appending = examples.iloc[batch_now.shape[0]:(batch_now.shape[0] + batchsize), :]
        batches.append(appending)
        print(appending.shape)
    else :
        appending = examples.iloc[batch_now.shape[0]:examples.shape[0], :]
        batches.append(appending)
        print(appending.shape)

#1. 함수 선언
#(1). API 호출함수 using requests.get
def collectinfor(sigunguCd, bjdongCd, startDate, endDate, key) :
    #(1). 호출 URL
    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo'

    #(2). 호출 파라미터 
    params = {'serviceKey': key,'numOfRows': '1000', 'pageNo': 1, 'sigunguCd': sigunguCd, 
            'bjdongCd': bjdongCd, "_type" : "json", "startDate" : startDate,"endDate":endDate}

    #(3). 헤더 설정
    hdr = {'User-Agent' : generate_user_agent(os="win", device_type="desktop")}

    #(4). 호출
    response = requests.get(url, params = params, headers=hdr)

    #(5). 파싱
    try :
        data = response.json()
        d = data['response']['body']['items']
        if len(d) == 0 : 
            return "nothing"
        else : 
            a = d['item']
            dat = pd.DataFrame(a)
            dat = dat[need]
            return dat
    except :
        soup = BeautifulSoup(response.text, 'html.parser')
        html_now = soup.get_text
        html_now = str(html_now)
    
        string1 = "<returnauthmsg>"
        string2 = "</returnauthmsg>"
        error_name = re.search('{}(.*){}'.format(string1, string2), string=html_now).group(1)
    
        string3 = "<returnreasoncode>"
        string4 = "</returnreasoncode>"
        error_number = re.search('{}(.*){}'.format(string3, string4), string=html_now).group(1)
    
        return str(sigunguCd) + "/" + str(bjdongCd) + "/" + error_name + "/" + error_number

#(2). API 호출함수 using urlopen
def collectinfor2(sigunguCd, bjdongCd, startDate, endDate, key) :
    #(1). 호출 URL 작성
    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo'

    #(2). 호출 파라미터 
    params = {'serviceKey': key,'numOfRows': '10000', 'pageNo': 1, 'sigunguCd': sigunguCd, 'bjdongCd': bjdongCd, "_type" : "json", "startDate" : startDate,"endDate":endDate}

    #(3). 인코딩
    urlencoding = urlencode(params)
    url = url + "?" + urlencoding

    #(4). 헤더설정
    hdr = {'User-Agent' : generate_user_agent(os="win", device_type="desktop")}

    #(5). 호출
    req = Request(url = url, headers=hdr)
    reqdata = urlopen(req).read().decode('utf-8')

    #(6). 파싱
    try :
        dic = json.loads(reqdata)
        d = dic['response']['body']['items']
        if len(d) == 0 : 
            return "nothing"
        else : 
            a = d['item']
            dat = pd.DataFrame(a)
            dat = dat[need]
            return dat
    except :
        soup = BeautifulSoup(reqdata, 'html.parser')
        html_now = soup.get_text
        html_now = str(html_now)
    
        string1 = "<returnauthmsg>"
        string2 = "</returnauthmsg>"
        error_name = re.search('{}(.*){}'.format(string1, string2), string=html_now).group(1)
    
        string3 = "<returnreasoncode>"
        string4 = "</returnreasoncode>"
        error_number = re.search('{}(.*){}'.format(string3, string4), string=html_now).group(1)
    
        return str(sigunguCd) + "/" + str(bjdongCd) + "/" + error_name + "/" + error_number

#(3). batch 별로 결과 리스트를 반환할 함수(remote 처리)
@ray.remote
def dat_final_make(examples, key1, key2, key3, startDate, endDate, need) :
    m = 0
    dat_full_collect = []

    while True :
        time.sleep(5)
        scope = range(m, examples.shape[0])

        for u in scope :
            if u % 3 == 0 :
                key = key1
            elif u % 3 == 1 :
                key = key2
            else :
                key = key3

            sigungu = examples.iloc[u,0]
            bjdong = examples.iloc[u,1]

            try :
                dat = collectinfor(sigunguCd=sigungu, bjdongCd=bjdong,
                                    startDate=startDate, endDate=endDate, key = key)
                dat_full_collect.append(dat)
            except :
                try : 
                    if u % 3 == 1 :
                        key = key1
                    elif u % 3 == 2 :
                        key = key2
                    else :
                        key = key3
                
                    dat = collectinfor2(sigunguCd=sigungu, bjdongCd=bjdong,
                                        startDate=startDate, endDate=endDate, key = key)
                    dat_full_collect.append(dat)
                except :
                    m = u
                    break
        
        if len(dat_full_collect) >= examples.shape[0] :
            break
        
    return dat_full_collect

#%% API 호출(병렬처리)
refs = []

for t in batches :
    refs.append(dat_final_make.remote(examples=t, key1= key1, key2 = key2, key3= key3,
                                    startDate = startDate, endDate = endDate, need = need))

returns = ray.get(refs)

#%% 데이터 정리
return_collection = []
for i in returns :
    target = i
    for j in range(len(target)) :
        return_collection.append(target[j])
        
len(return_collection)

#1. 데이터프레임과 아닌 것들 나누기
dataframe = []
nonframe =[]

for i in range(len(return_collection)) :
    target = return_collection[i]

    if isinstance(target, pd.DataFrame) :
        dataframe.append(target)
    else :
        nonframe.append(target)

#(1). 데이터프레임 정리
dat_final = pd.concat(dataframe)

#업데이트 날짜를 열로 붙이자
now = time.localtime()
now = time.strftime('%Y%m%d', now)
dat_final.insert(0,'update_time', now)
dat_final.head(2)

#(2). non데이터프레임 정리
non_pass = []

for i in nonframe :
    target = i
    if target != "nothing" :
        non_pass.append(target)

#(3). 에러 처리
non_sigungu = []
non_bjdong = []
non_error_name = []
non_error_num = []

for i in non_pass :
    target = i
    target = target.split("/")
    
    non_sigungu.append(target[0])
    non_bjdong.append(target[1])
    non_error_name.append(target[2])
    non_error_num.append(target[3])

non_pass_dic = {}
non_pass_dic['sigunguCd'] = non_sigungu
non_pass_dic['bjdongCd'] = non_bjdong
non_pass_dic['error_name'] = non_error_name
non_pass_dic['error_num'] = non_error_num

dat_error = pd.DataFrame(non_pass_dic)

#업데이트 날짜 추가
now = time.localtime()
now = time.strftime('%Y%m%d', now)
dat_error.insert(0, "update_date", now)
dat_error.head(3)

#7. DB에 데이터 적재
con = pymysql.connect(host = "localhost", user = "root", password="0000", db = "data_current", charset='utf8')
cur = con.cursor()

#(1). 데이터프레임 적재
for i in range(dat_final.shape[0]) :
    target = dat_final.iloc[i,:]
    target = tuple(target)
    try : 
        query = """
        INSERT INTO 전용면적(update_date, area, bjdongCd, bldNm, etcPurps, exposPubuseGbCd, 
        exposPubuseGbCdNm,flrGbCdNm,mainAtchGbCd,mainAtchGbCdNm, mainPurpsCd, 
        mainPurpsCdNm, mgmBldrgstPk, newPlatPlc, platPlc, sigunguCd)
        VALUES {}
        """.format(target)
        cur.execute(query)
        con.commit()
    except : 
        print(i)
        next

#(2). 에러 적재
for i in range(dat_error.shape[0]) :
    target = dat_error.iloc[i,:]
    target = tuple(target)
    
    try : 
        query = """
            INSERT INTO 전용면적_에러(update_date, sigunguCd, bjdongCd, error_name, error_num) VALUE {}
        """.format(target)
        cur.execute(query)
        con.commit()
    except :
        print(target)
        next

con.close()

#8. 날짜를 업데이트 한다
update_time = time.localtime()
update_time = time.strftime('%Y%m%d', update_time)
print(update_time)

con = pymysql.connect(host = "localhost", user = "root", password="0000", 
                    db = "infor", charset='utf8')
cur = con.cursor()

query = """
    UPDATE date SET last = {}
""".format(update_time)
cur.execute(query)
con.commit()
con.close()