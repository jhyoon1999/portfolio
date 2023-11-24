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
    st.markdown("""
                - 프로젝트 내용 
                    - 전국 아파트 부동산 매매/전세 거래 데이터 수집 및 시각화
                    - 유저(User) 특성별 아파트 선호도 조사
                    - 선호도 기반 아파트 추천 시스템 개발
                """)
    st.markdown('- 주요 언어 : Python, R')
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('Ⅱ. 담당업무')
    st.markdown("- 데이터 수집")
    st.markdown("- 아파트와 그 주변시설 시각화")

#%% WBS

with tab2 :
    st.image('src/apartment_AI/WBS_apartment.png')


#%% 프로젝트 진행

with open("src/apartment_AI/geocode.r", "r", encoding='utf-8') as r_code :
    api_r_code = r_code.read()

with open("src/apartment_AI/update_code.py", 'r', encoding='utf-8') as file :
    python_code = file.read()

with tab3 :
    col1, arrow1, col2, arrow2, col3 = st.columns(5)
    
    with col1 :
        f = st.button(label = "프로젝트 목표 및 데이터 수집", key = "first", type = "primary")
    with arrow1 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col2 :
        s = st.button(label = "데이터 수집", key = "second", type = "primary")
    with arrow2 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col3 :
        t = st.button(label = "데이터 시각화", key = "third", type = "primary")

    if f :
        st.markdown("""
                    - 프로젝트 목표 
                        - 전국 아파트 부동산 매매/전세 거래 데이터 수집 및 시각화
                        - 유저(User) 특성별 아파트 선호도 조사
                        - 선호도 기반 아파트 추천 시스템 개발
                    """)
        
        st.markdown("""
                    - 데이터 수집
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
    
    if s :
        st.markdown("""
                    - 전국 아파트 GPS 데이터 수집코드
                        - 사전 수집된 전국 아파트 부동산 매매/전세 거래 데이터에 존재하는 지번주소를 활용
                        - 카카오 지도 API를 이용해 지오코딩을 실시하며, 과도한 트래픽으로 인한 밴을 막기 위해 순차 진행하는 for문 사용
                    """)
        st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        st.code(api_r_code, language='r')
        st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 아파트 데이터 업데이트
                        - DB 내의 아파트 정보가 업데이트 되었을 때 API를 호출해 데이터를 갱신
                    """)
        st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
        st.code(python_code, language="python")
    
    if t :
        st.markdown("""
                    - 수집한 아파트 및 주변시설을 지도에 나타내는 시각화 진행
                    - Power BI 활용
                    """)
        col1, col2 = st.columns(2)
        with col1 :
            st.image('src/apartment_AI/vis_1.png')
        with col2 : 
            st.image("src/apartment_AI/vis_2.png")