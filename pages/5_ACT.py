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
    <td>2021.10 ~ 2021.12</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">머신러닝을 활용해 기존 검사방식의 20% 길이의 인지검사 시스템 개발 </td> 
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
        st.progress(value=100, text = "데이터 분석(100%)")
        st.progress(value=100, text = "알고리즘 구현(100%)")
        st.progress(value=100, text = "적응적 검사 개발(100%)")
        st.progress(value=100, text = "보고서 작성(100%)")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/WBS_ACT.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 결과물")
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
                    <p style="font-weight:normal;">{"〮수집 데이터의 통계적 가정 검증 → 의사결정나무(Decision Tree) 기반 개발이 적절"}</p>
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
                    <p style="font-weight:normal;">{"〮Yan(2004)의 Merged Decision Tree 구현 : 데이터 크기로 인한 과적합(overfit) 최소화"}</p>
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
                    <p style="font-weight:normal;">{"〮9개 인지영역 별 최선의 알고리즘 탐색 및 선택"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/portfolio/master/src/ACT/algorithm_comparison.png" alt="image" style="max-width:100%; max-height:400px;">
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
                    <p style="font-weight:normal;">{"〮보고서 및 Working Technical Document 작성"}</p>
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