import streamlit as st
from st_pages import add_page_title
import pandas as pd

add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행","코드"])

#%%1. 요약

qualitative_summary = """
<style>
  table {
      width: 100%;
      border-collapse: collapse;
  }
  
  th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: left;
  }
  
  th {
      background-color: #808080;
      color: white;
  }
</style>

<table>
  <tr>
    <th>진행기간</th>
    <td>2023.04-2023.07(4개월)</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">텍스트 답변의 토픽, 감성을 자동 라벨링 하는 분석 플랫폼 구축</td> 
  </tr>
  <tr>
    <th>사용언어</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/python_logo.png" alt="Python Image" width="80" height="50">
    </td>
  </tr>
  <tr>
    <th>데이터베이스</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/Mysql_logo.png" alt="MySQL Image" width="80" height="50">
    </td>
  <tr>
    <th>BI 툴</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/powerbi_logo.png" alt="PowerBI Image" width="80" height="50">
    </td>
  </tr>
</table>
"""

@st.cache_data
def call_qualitative_result() :
    qualitative_result = pd.read_excel("src/qualitative_AI/qualitative_result_example.xlsx")
    return qualitative_result

qualitative_result = call_qualitative_result()
    
with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 요약")
        st.markdown(qualitative_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=50, text = "학습 도메인/프로젝트 선정(50%)")
        st.progress(value=50, text = "데이터 수집/관리(50%)")
        st.progress(value=70, text = "통합 라벨링 체계 구축(70%)")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. 프로젝트 개요")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/qualitative_AI/overview_qualitative.png", use_column_width="auto")
    

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/qualitative_AI/WBS_qualitative.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("IV. 결과물(예시)")
    st.dataframe(qualitative_result)

#%%2. 프로젝트 진행

with tab2 :
    #(1). 도메인/프로젝트 선정
    fcol1, fcol2 = st.columns([2,8])
    with fcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"도메인/프로젝트 선정"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with fcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:bold;">{"목적 : LLM모델이 학습할 리서치의 도메인과 그 하위 프로젝트 선정"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/qualitative_AI/table_project.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(2). 데이터 수집/검수
    scol1, scol2 = st.columns([2,8])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 수집/검수"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                        <p style="font-weight:bold;">{"목적 : 선정한 프로젝트의 데이터를 수집후, 학습 가능한 구조로 변환 및 검수"}</p>\
                        <p style="font-weight:normal;">{"〮각 도메인의 프로젝트 로컬 데이터를 수집 후 Python을 이용해 구조 변환 및 검수 진행"}</p>\
                        <p style="font-weight:normal;">{"〮실시간 수집 현황을 확인할 수 있는 수집 데이터 관리 대시보드 작성 및 운영"}</p>\
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/qualitative_AI/powerbi_process.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(4). 통합 라벨 체계 구성
    focol1, focol2 = st.columns([2,8])
    with focol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"통합 라벨 체계 구성"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with focol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:bold;">{"목적 : 각 도메인 별로 학습 가능한 수준의 통합 라벨 체계 구축"}</p>\
                    <p style="font-weight:normal;">{"〮각 프로젝트 별 독자적인 라벨 체계 존재 → 타부서와의 협력을 통해 각 도메인 별 통합 라벨 체계 구축"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/qualitative_AI/label_process.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%%3. 코드
import requests

@st.cache_resource
def call_cleaning_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/2_AI_Qualitative_Data_Labeling_Platform/master/%EC%88%98%EC%A7%91%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B2%80%EC%88%98%20%EC%BD%94%EB%93%9C.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_preprocessing_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/2_AI_Qualitative_Data_Labeling_Platform/master/%ED%85%8D%EC%8A%A4%ED%8A%B8_%EC%A0%84%EC%B2%98%EB%A6%AC.py"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_clustering_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/2_AI_Qualitative_Data_Labeling_Platform/master/%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81_DBSCAN.py"
    response = requests.get(github_url)
    code = response.text
    return code

cleaning_code = call_cleaning_python()
preprocessing_code = call_preprocessing_python()
clustering_code = call_clustering_python()

with tab3 :
    st.write("#### 1. 데이터 검수")
    with st.expander("수집 데이터 검수 코드") :
        st.code(cleaning_code, language = "python")
    
    st.write("#### 2. 데이터 분석")
    with st.expander("텍스트 전처리") :
        st.code(preprocessing_code, language = "python")
    with st.expander("DBSCAN 클러스터링") :
        st.code(clustering_code, language = "python")