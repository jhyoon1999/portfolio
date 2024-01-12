import streamlit as st
from st_pages import add_page_title


add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행","코드"])

#%% 1. 요약

JWI_summary = """
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
    <td>2022.06 ~ 2022.12</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">COVID-19 사태 전/후 의류산업 변동 분석</td> 
  </tr>
  <tr>
    <th>사용언어</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/R_logo.jpg" alt="R Image" width="80" height="50">
    </td>
  </tr>
  <tr>
    <th>앱 개발</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/shiny_logo.png" alt="Shiny Image" width="80" height="50">
    </td>
</table>
"""


with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 요약")
        st.markdown(JWI_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=30, text = "데이터 수집/가공(30%)")
        st.progress(value=80, text = "분석 앱 개발(80%)")
        st.progress(value=70, text = "인사이트 도출(70%)")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/WBS_JWi.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 결과물")
    with st.expander("01)분석 앱") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/app_vis.png", use_column_width="auto")
    with st.expander("02)인사이트 보고서") :
        st.image("https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/insight_img.png", use_column_width="auto")

#%%2. 프로젝트 진행
with tab2 :
    #(1). 데이터 수집/가공
    fcol1, fcol2 = st.columns([2,8])
    with fcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"데이터 수집/가공"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with fcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮데이터 수집 : 국내 의류산업 내 기업들의 연도별 기본 및 재무정보"}</p>
                </div>
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮데이터 검수"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/missing_value.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮기업 건전성 변수 생성"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/variable_img.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(2). 분석 앱 개발
    scol1, scol2 = st.columns([2,8])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"분석 앱 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮클라이언트가 여러 시나리오 하에서 각종 통계분석/시각화를 진행할 수 있는 분석 앱 개발"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/app_vis.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(3). 인사이트 도출
    tcol1, tcol2 = st.columns([2,8])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"인사이트 도출"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">
                <div style="position:relative; text-align:left;">
                    <p style="font-weight:normal;">{"〮ML(XgBoost, Randomforest)을 이용해 COVID-19 전/후를 나누는 주요 기업 건전성 지표 식별 및 인사이트 발견"}</p>
                </div>
                <div style="position:relative; text-align:center;">
                    <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/JWi/insight_img.png" alt="image" style="max-width:100%; max-height:400px;">
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%%3. 코드
import chardet

with open("src/JWi/app.R", 'rb') as file:
    result = chardet.detect(file.read())

encoding = result['encoding']

with open("src/JWi/app.R", 'r', encoding=encoding) as file:
    app_code = file.read()

with tab3 :
    with st.expander("RShiny 코드") :
        st.code(app_code, language = "r")