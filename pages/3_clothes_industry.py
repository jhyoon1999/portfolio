import streamlit as st
from st_pages import add_page_title


add_page_title(layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["개요", "WBS", "프로젝트 진행","기타"])

#%% 개요

with tab1 :
    st.subheader("Ⅰ. 프로젝트 개요")
    st.markdown("- 프로젝트명 : 국내 의류산업 현황 분석 및 분석 앱 개발")
    st.markdown("- 프로젝트 기간 : 2022.06 ~ 2022.12")
    st.markdown("- 프로젝트 발주 : 데이터바우처 사업-AI가공-에 공급기업으로 참여하여 스타트업 수요기업에 데이터 서비스 제공")
    st.markdown("""
                - 프로젝트 내용
                    - 국내 의류산업(도소매, 제조) 기업들에 대한 데이터 분석 앱 개발
                    - COVID-19 시대 이전과 이후 사이의 의류산업 변동에 대한 인사이트 발견
                """)
    st.markdown("- 주요언어 : R")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. 담당업무")
    st.markdown("- 의류 산업 기업의 기본, 재무 정보 데이터 수집")
    st.markdown("- 국내 의류 산업 기업의 데이터 분석 앱 개발")
    st.markdown("- ML 기반 데이터 마이닝")
    st.markdown("- 의류 산업 현황에 대한 인사이트 보고서 작성")

#%% WBS
with tab2 :
    st.image("src/JWi/WBS_JWi.png")

#%% 프로젝트 진행
with tab3 :
    col1, arrow1, col2, arrow2, col3, arrow3, col4 = st.columns(7)
    
    with col1 :
        f = st.button(label = "데이터 수집", key = "first", type = "primary")
    with arrow1 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col2 :
        s = st.button(label = "데이터 분석 앱 개발", key = "second", type = "primary")
    with arrow2 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col3 :
        t = st.button(label = "데이터 마이닝", key = "third", type = "primary")
    with arrow3 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col4 :
        fo = st.button(label = "보고서 작성", key = "fourth", type = "primary")
    
    if f :
        st.markdown("""
                    - 데이터 수집
                        - 필요 데이터 : 국내 의류 산업 내 기업들의 연도별 기본 및 재무 정보
                        - 구매처 : 나이스디앤비
                    """)
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        st.markdown("""
                    - 구매 데이터 정보
                        - 데이터 내 기업 수 : 10,353개
                        - 주요 사업군 별 기업 수
                    """)
        st.image("src/JWi/industry_vis.png", use_column_width="auto")
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        st.markdown("""
                    - 구매 데이터 검수 
                    """)
        st.image("src/JWi/missing_value.png", use_column_width="auto")
    
    if s :
        st.markdown("""
                    - 목표 : 클라이언트가 실시간으로 활용할 수 있는 분석 앱 개발
                    - RShiny 활용
                    - shinyapps.io를 통해 배포
                    """)
        
        st.markdown("- 분석 앱 이미지")
        st.image("src/JWi/app_vis1.png", use_column_width="auto")
        st.markdown('<hr style="border: 0.5px dashed #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        st.image("src/JWi/app_vis2.png", use_column_width="auto")
        st.markdown('<hr style="border: 0.5px dashed #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        st.image("src/JWi/app_vis3.png", use_column_width="auto")
    
    if t :
        st.markdown("""
                    - 목표 : COVID-19 이전과 이후 사이의 국내 의류산업 변동에 대한 인사이트 발견
                    - 앙상블 기법(Ex. Randomforest, XGboost)을 이용해 COVID-19 이전과 이후를 나누는 주요 기업 재무정보 식별
                    - 해당 기업 재무정보의 COVID-19 이전과 이후 시각화
                    """)
        
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 주요 기업 건전성 지표 정의 : 한국은행 2019년 기업경영분석결과(해설 및 통계편) 참조
                    - COVID-19 이전, 이후 기업 데이터 라벨링 후 ML 학습 진행
                    - 변수 중요도(Variable Importance) 산출
                    """)
        
        st.image("src/JWi/ai_vis1.png", use_column_width="auto")
        st.image("src/JWi/ai_vis2.png", use_column_width="auto")
    
    if fo :
        st.markdown("- 데이터마이닝 결과 기반 인사이트 보고서 작성")
        column1, column2 = st.columns(2)
        with column1 :
            st.image("src/JWi/report_vis1.png", use_column_width="auto")
        with column2 :
            st.image("src/JWi/report_vis2.png", use_column_width="auto")
        


#%% 기타
import chardet

with open("src/JWi/app.R", 'rb') as file:
    result = chardet.detect(file.read())

encoding = result['encoding']

with open("src/JWi/app.R", 'r', encoding=encoding) as file:
    app_code = file.read()

with tab4 :
    with st.expander("RShiny 코드") :
        st.code(app_code, language = "r")