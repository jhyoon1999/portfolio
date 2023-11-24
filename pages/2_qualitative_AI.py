import streamlit as st
from st_pages import add_page_title

add_page_title(layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["개요", "WBS", "프로젝트 진행","기타"])

#%% 개요

with tab1 : 
    st.subheader('Ⅰ. 프로젝트 개요')
    st.markdown("- 프로젝트명 : AI 기반 리서치 정성데이터 분석 플랫폼 구축")
    st.markdown('- 프로젝트 기간 : 2023.04 ~ 2023.10')
    st.markdown("""
                - 문제상황
                    - 많은 리서치 클라이언트는 고객의 직접적인 의견 수집을 요구하며, 정성문항은 각 설문조사의 30%를 차지함
                    - 조사 후 정성문항 답변에 대한 라벨링(주제, 감성) 작업은 많은 시간과 비용을 요구
                """)
    st.markdown("""
                - 프로젝트 발주 : AI바우처 사업에 수요기업으로 지원하여, 공급기업과 함께 정성데이터 분석 플랫폼 구축
                """)
    st.markdown("""
                - 프로젝트 내용
                    - 리서치 정성문항 통합 라벨링 체계 확립
                    - LLM 기반 정성문항 분석(주제, 감성) AI 개발
                    - 리서치 정성데이터 분석 플랫폼 개발
                """)
    st.markdown("- 주요 언어 : python")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. 담당업무")
    st.markdown("""
                - 사업계획서 작성
                - 데이터 수집 및 검수
                - 리서치 정성문항 통합 라벨링 체계 구성
                - ML 학습결과 해석 및 피드백
                """)
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

#%% WBS

with tab2 :
    st.image("src/qualitative_AI/WBS_qualitative.png")


#%% 프로젝트 진행

with tab3 :
    col1,arrow1, col2, arrow2,col3, arrow3, col4= st.columns(7)
    
    with col1 :
        f = st.button(label = "사업계획서 작성", key = "first", type="primary")
    
    with arrow1 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    
    with col2 :
        s = st.button(label = "도메인 선정 및 데이터 수집", key = "second", type="primary")
    
    with arrow2 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    with col3 : 
        t = st.button(label = "통합분류체계구성", key = "third", type="primary")
        
    with arrow3 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    with col4 : 
        fo = st.button(label = "운영환경구축", key = "fourth")
    
    # 프로젝트 목표 및 사업계획서 작성
    if f :
        st.markdown("""
                    - 프로젝트 목표
                        - 리서치 정성문항 통합 라벨링 체계 확립 : 수요기업 담당
                        - LLM 기반 정성문항 분석(주제, 감성) AI 개발 : 공급기업 담당
                        - 리서치 정성데이터 분석 플랫폼 개발 : 공통
                    """)
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        st.markdown("""
                    - 사업계획서 작성 및 발표(기여도 : 40%)
                    """)
        column1, column2 = st.columns(2)
        
        with column1 :
            st.image("src/qualitative_AI/plan_vis.png")
        
        with column2 :
            st.image("src/qualitative_AI/ppt_vis.png")
    
    # 도메인 선정 및 데이터 수집
    if s :
        st.markdown("""
                    - 목표 : AI 학습 대상 리서치 도메인 및 프로젝트 선정
                    - 도메인 선정기준
                        - 포괄성 : 많은 타도메인, 타프로젝트를 포괄할 수 있는 포괄성이 높은 도메인
                        - 미래지향성 : 지속가능성이 높은 클라이언트 보유 도메인
                        - 공통성 : 공통적인 질문 및 답변이 많이 발생하는 도메인
                    - 프로젝트 선정기준
                        - 유사성 : 도메인 내 비슷한 질문 및 답변을 갖는 프로젝트
                        - 완결성 : 데이터 완성도(Ex. 결측치)가 뛰어난 데이터를 보유한 프로젝트
                    """)
        st.markdown("- 5개 도메인과 그 하위 445개 프로젝트 선정 및 수집")
        _,col1,_ = st.columns([2,6,2])
        with col1 :
            st.image("src/qualitative_AI/table_project.png", use_column_width="auto")
    
    # 통합분류체계구성
    
    if t :
        st.markdown("""
                    - 문제상황 : 프로젝트 단위로 독자적인 정성문항 답변 분류체계 존재
                    - 목표 : 각 도메인 별로 AI가 학습할 통합 분류체계 구성
                    - 프로세스
                    """)
        
        _,col1,_ = st.columns([2,6,2])
        with col1 :
            st.image("src/qualitative_AI/process_ai.png")

        st.markdown("""
                    - 결과 : 토픽 분류 AI 학습이 가능한 도메인 별 통합분류체계 구성완료
                    """)

#%% 기타
with open("src/qualitative_AI/cleaning.py", 'r', encoding='utf-8') as cleaning_read:
    cleaning_code = cleaning_read.read()

with tab4 :
    with st.expander("수집 데이터 검수 코드") :
        st.code(cleaning_code, language = "python")