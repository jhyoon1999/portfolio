import streamlit as st
from st_pages import add_page_title

add_page_title(layout = "wide")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["개요", "WBS", "프로젝트 진행",
                                        "제품 출시", "기타"])

#%% 개요

with tab1 :
    st.subheader('Ⅰ. 프로젝트 개요')
    st.markdown("- 프로젝트명 : 예측모델링 알고리즘을 활용한 종합 적응적 인지검사 시스템 ACT 개발")
    st.markdown('- 프로젝트 기간 : 2021.10 ~ 2021.12')
    st.markdown('- 프로젝트 내용 : 의사결정나무(Decision-Tree) 알고리즘을 이용해 기존 검사보다 80% 짧은 길이의 적응적 인지검사 시스템(ACT) 개발')
    st.markdown('- 주요 언어 : R')
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('Ⅱ. 담당업무')
    st.markdown("- 수집 데이터 분석")
    st.markdown("- 논문 알고리즘 구현")
    st.markdown("- 적응적 인지검사 ACT 개발")
    st.markdown("- 결과 보고서 작성")
    st.markdown("- Working Technical Document 작성")

#%% WBS
with tab2 :
    st.image('src/ACT/WBS_ACT.png')

#%% 프로젝트 진행

with tab3 :
    col1, arrow1, col2, arrow2, col3, arrow3, col4, arrow4, col5  = st.columns(9)
    
    with col1 :
        f = st.button(label = "프로젝트 목표 및 데이터 구성", key = "first", type = "primary")
    with arrow1 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col2 :
        s = st.button(label = "데이터 분석", key = "second", type = "primary")
    with arrow2 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col3 :
        t = st.button(label = "논문 알고리즘 구현", key = "third", type = "primary")
    with arrow3 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    with col4 :
        fo = st.button(label = "ACT 개발", key = "fourth", type = "primary")
    with arrow4 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col5 :
        fif = st.button(label = "보고서 작성", key = "fifth", type = "primary")
    
    
    if f :
        st.markdown("""
                    - 프로젝트 목표
                        - 대상으로 하는 9개 인지검사 영역 별로 컴퓨터 기반 적응적 검사(CAT) 개발
                        - 종합 적응적 인지검사 시스템 ACT 개발
                    """)
        st.image("src/ACT/Purpose_ACT.png")
        
        st.markdown("""
                    - 데이터 구성
                    """)
        st.image("src/ACT/Data_ACT.png")
    
    if s :
        st.markdown("""
                - 적응적 검사 개발 방향
                    - 강력한 통계적 가정을 요구하는 문항반응이론(Item Response Theory)에 기반을 둔 적응적 검사 구현 불가
                    - 대안으로 통계적 가정을 요구하지 않는 의사결정나무(Decision Tree) 기반 적응적 검사 개발 필요
                """)
        st.markdown("""
                    - 과적합 문제
                        - 각 검사 영역별 학습데이터가 충분치 않아 이른 과적합 발생 확인
                        - 일반적인 의사결정나무 알고리즘으로는 충분한 예측성능 달성 불가
                    """)
        st.image("src/ACT/generalDT_ACT.png")
        st.markdown("<div style='text-align:center;'><h10><strong>일반적인 의사결정나무 기반 적응적 검사</strong></h10></div>", unsafe_allow_html=True)
    
    if t :
        st.markdown("""
                    - 논문 탐색
                        - Yan(2004)이 제시한 Merged Decision Tree 알고리즘이 데이터 부족으로 인한 과적합 문제 억제
                    - 알고리즘 구현
                        - Merged Decision Tree를 R을 이용해 구현 완료
                    """)
        st.image("src/ACT/Merged_DT_ACT.png")
        st.markdown("<div style='text-align:center;'><h10><strong>Merged Decision Tree 기반 적응적 검사</strong></h10></div>", unsafe_allow_html=True)
    
    if fo :
        st.markdown("""
                    - 각 인지검사 영역별로 Merged Decision Tree 기반 적응적 검사 개발
                    - 적응적 검사의 추정 예측성능 산출
                    """)
        
        st.image("src/ACT/cor_ACT.png")
        st.image("src/ACT/MAE_ACT.png")
        st.image("src/ACT/RMSE_ACT.png")
    
    if fif :
        
        col1, col2 = st.columns([5,5])
        with col1 : 
            st.markdown("- 결과 보고서 작성")
            st.image("src/ACT/result_document.png")
        
        with col2 :
            st.markdown("- Working Technical Document 작성")
            st.image("src/ACT/Technical_ACT.png")

#%% 제품 출시

with tab4 :
    with st.expander("0. ACT 공식 홈페이지(http://211.169.249.237/site/defaultMain.do)") :
        st.components.v1.html('<iframe src="http://211.169.249.237/site/defaultMain.do" width="1500" height="600"></iframe>', height=600)
    
    with st.expander("1. ACT 소개 페이지(http://psyctest.orp.co.kr/introduce/view/?s=40)") :
        st.components.v1.html('<iframe src="http://psyctest.orp.co.kr/introduce/view/?s=40" width="1500" height="600"></iframe>', height=600)
#%% 기타

with tab5 : 
    with st.expander("참여증빙서류") :
        st.image("src/ACT/participation_ACT.jpg")