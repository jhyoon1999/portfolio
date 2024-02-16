import streamlit as st
from st_pages import add_page_title

add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행","코드"])

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
    <td>2021.10-2021.12(3개월)</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">기존검사 대비 20% 소요시간을 갖는 ML기반 인지능력 검사 시스템 개발</td> 
  </tr>
  <tr>
    <th>사용언어</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/R_logo.jpg" alt="R Image" width="80" height="50">
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
        st.progress(value=80, text = "데이터 분석(80%)")
        st.progress(value=90, text = "알고리즘 구현(90%)")
        st.progress(value=70, text = "적응적 검사 개발(70%)")
        st.progress(value=90, text = "보고서 작성(90%)")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

    st.subheader("Ⅱ. 프로젝트 개요")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/overview_ACT.png", use_column_width="auto") ##추후 수정##

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/WBS_ACT.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("IV. 결과물")
    with st.expander("적응적 인지검사 시스템 ACT 출시") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/ACT_homepage.png", use_column_width="auto")

#%%2. 프로젝트 진행

with tab2 :
    #(1). 데이터 분석
    fcol1, fcol2 = st.columns([2,8])
    with fcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 분석"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with fcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                        <p style="font-weight:bold;">{"목적 : 데이터의 문항반응이론(Item Response Theory) 가정 충족 여부 확인 후, 검사 시스템 개발 방향 결정"}</p>\
                        <p style="font-weight:normal;">{"〮데이터 구조 파악을 위한 기초통계치 산출"}</p>\
                        <p style="font-weight:normal;">{"〮적응적 검사 개발의 일반적 접근인 문항반응이론의 가정 충족 여부 확인 → 불충족 확인"}</p>\
                        <p style="font-weight:normal;">{"〮적응적 검사의 형태를 갖는 머신러닝 모델 의사결정나무(Decision Tree) 기반 검사 시스템 개발 결정"}</p>\
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/assumption_result.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(2). 알고리즘 구현
    scol1, scol2 = st.columns([2,8])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"알고리즘 구현"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                        <p style="font-weight:bold;">{"목적 : 의사결정나무의 데이터 크기에 따른 과적합(Overfit) 문제를 억제할 수 있는 Merged Decision Tree 알고리즘 구현"}</p>\
                        <p style="font-weight:normal;">{"〮Yan(2004)이 제시한 Merged Decision Tree 알고리즘이 의사결정나무의 과적합 발생을 억제할 수 있음을 발견"}</p>\
                        <p style="font-weight:normal;">{"〮구현 언어 : R"}</p>\
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/merged_tree.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(3). 적응적 검사 개발
    tcol1, tcol2 = st.columns([2,8])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"적응적 검사 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                        <p style="font-weight:bold;">{"목적 : 각 인지능력 영역별 최적의 알고리즘 탐색 후, 최종 모델 기반 적응적 검사 개발"}</p>\
                        <p style="font-weight:normal;">{"〮각 인지영역 별로 모델 성능 비교 후, 최종 모델 선정"}</p>\
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/development_ACT.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(4). 보고서 작성
    focol1, focol2 = st.columns([2,8])
    with focol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"보고서 작성"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with focol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:bold;">{"〮목적 : 제품 출시를 위한 1)개발 보고서, 2)Working Technical Document 작성"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/document_img.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%%3. 코드
import requests

@st.cache_resource
def call_merged_tree_r() :
    github_url = "https://raw.githubusercontent.com/jhyoon1999/5_ACT_Development_of_Adaptive_Cognitive_Test_System/master/Merged_Decision_Tree_%EA%B5%AC%ED%98%84_Code.r"
    response = requests.get(github_url)
    code = response.text
    return code

merged_tree_code = call_merged_tree_r()

with tab3 :     
    with st.expander("Merged Decision Tree 구현 코드") :
        st.code(merged_tree_code, language = "r")