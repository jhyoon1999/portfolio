import streamlit as st
from st_pages import add_page_title


add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행", "코드"])

#%%1. 요약
apartment_summary = """
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
    <td>2022.06 ~ 2022.12(6개월)</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">이용자 선호도 기반 아파트 추천시스템 개발</td> 
  </tr>
  <tr>
    <th>사용언어</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/python_logo.png" alt="Python Image" width="80" height="50">
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/R_logo.jpg" alt="R Image" width="80" height="50">
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

with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 요약")
        st.markdown(apartment_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=40, text = "데이터 수집(40%)")
        st.progress(value=80, text = "대시보드 개발 및 운영(80%)")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/apartment_AI/WBS_apartment.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 결과물")
    with st.expander("데이터 관리 대시보드") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/apartment_AI/dashboard.png", use_column_width="auto")

#%%2. 프로젝트 진행
with tab2 :
    #(1). 데이터 수집
    fcol1, fcol2 = st.columns([2,8])
    with fcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 수집"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with fcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮데이터 출처 : 공공데이터 포털, 카카오 지도"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/apartment_AI/process_apartment.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(2). 대시보드 개발
    scol1, scol2 = st.columns([2,8])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"대시보드 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮클라이언트가 수집 데이터 현황(지역별 아파트 및 그 외 시설)을 실시간으로 확인 가능한 대시보드 작성 및 운영"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/apartment_AI/dashboard.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%%3. 코드
import requests

@st.cache_resource
def call_kakao_api_r() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/4_Development-of-apartment-recommendation-system/master/%EC%B9%B4%EC%B9%B4%EC%98%A4%EC%A7%80%EB%8F%84_API_%EC%9A%94%EC%B2%AD_%EC%BD%94%EB%93%9C.r"
    response = requests.get(github_url)
    code = response.text
    return code

@st.cache_resource
def call_DB_update_python() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/4_Development-of-apartment-recommendation-system/master/DB_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8_%EC%BD%94%EB%93%9C.py"
    response = requests.get(github_url)
    code = response.text
    return code

kakao_api_code = call_kakao_api_r()
db_update_code = call_DB_update_python()

with tab3 :
    with st.expander("시설 지리정보 수집코드") :
        st.code(kakao_api_code, language = "r")

    with st.expander("DB 업데이트 코드") :
        st.code(db_update_code, language = "python")