import streamlit as st
from st_pages import add_page_title


add_page_title(layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["개요", "WBS", "프로젝트 진행",
                                "기타"])

#%% 개요

with tab1 :
    st.subheader('Ⅰ. 프로젝트 개요')
    st.markdown("- 프로젝트명 : AI 기반 맞춤형 아파트 분석 추천시스템")
    st.markdown('- 프로젝트 기간 : 2022.06 ~ 2022.12')
    st.markdown("- 프로젝트 발주 : 데이터바우처 사업-AI가공-에 공급기업으로 참여하여 스타트업 수요기업에 데이터 서비스 제공")
    st.markdown("""
                - 프로젝트 내용 
                    - 전국 아파트 부동산 매매/전세 거래 데이터 수집 및 시각화
                    - 유저(User) 특성별 아파트 선호도 조사
                    - 선호도 기반 아파트 추천 시스템 개발
                """)
    st.markdown('- 주요 언어 : Python, R')
    st.markdown("- BI툴 : Power BI")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('Ⅱ. 담당업무')
    st.markdown("- 데이터 수집")
    st.markdown("- 아파트와 그 주변시설 시각화")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

#%% WBS

with tab2 :
    st.image('src/apartment_AI/WBS_apartment.png', use_column_width= "auto")


#%% 프로젝트 진행

with tab3 :
    col1, arrow1, col2, arrow2, col3, arrow3, col4 = st.columns(7)
    
    with col1 :
        f = st.button(label = "데이터 수집", key = "first", type = "primary")
    with arrow1 :
        st.markdown("  ➡️  ")

    with col2 :
        s = st.button(label = "데이터 시각화", key = "second", type = "primary")
    with arrow2 :
        st.markdown("  ➡️  ")
    
    with col3 :
        t = st.button(label = "선호도 조사", key = "third")
    with arrow3 :
        st.markdown("  ➡️  ")
        
    with col4 :
        fo = st.button(label = "추천시스템 개발", key = "fourth")

    if f :
        st.markdown("""
                    - 데이터 수집 목록
                        - 전국 아파트 부동산 매매/전세 거래 데이터
                            - 출처 : 공공데이터포털
                            - 수집방법 : Open API
                        
                        - 아파트 GPS 데이터
                            - 출처 : 카카오지도
                            - 수집방법 : Open API
                        
                        - 아파트 주변시설 데이터
                            - 출처 : 공공데이터포털
                            - 수집방법 : Open API
                        
                        - 유저 아파트 선호도 데이터
                            - 수집 방법 : 설문조사
                    """)
        
        st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 데이터 수집 담당 목록
                        - 전국 아파트 GPS 데이터 수집
                        - 전용면적, 공급면적 데이터 수집
                        - 출처 내 데이터 갱신시 DB 데이터 업데이트 
                    """)
    
    if s :
        st.markdown("""
                    - 목표 : 클라이언트가 실시간으로 활용할 수 있는 수집데이터 시각화 자료 생성
                    - 사용 툴 : Power BI
                    - 시각화 내용 : 아파트 위치를 중심으로 반경 내의 주변시설 시각화(Haversine Formula 사용)
                    """)
        col1, col2 = st.columns(2)
        with col1 :
            st.image('src/apartment_AI/vis_1.png', use_column_width="auto")
        with col2 : 
            st.image("src/apartment_AI/vis_2.png", use_column_width="auto")

#%% 기타

with open("src/apartment_AI/geocode.r", "r", encoding='utf-8') as r_code :
    api_r_code = r_code.read()

with open("src/apartment_AI/update_code.py", 'r', encoding='utf-8') as file :
    python_code = file.read()

with tab4 :
    with st.expander("아파트 GPS 데이터 수집코드") :
        st.code(api_r_code, language = "r")

    with st.expander("DB 내 데이터 업데이트 코드") :
        st.code(python_code, language = "python")