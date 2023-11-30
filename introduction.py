import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

show_pages(
    [
        Page("introduction.py", "소개", "🏠"),        
        Section(name="참여 프로젝트", icon=":pig:"),
        Page("pages/1_travel_recommend.py", "제주도 여행지 추천 웹서비스 개발"),
        Page("pages/2_qualitative_AI.py", "AI기반 리서치 정성데이터 분석플램폼 구축"),
        Page("pages/3_clothes_industry.py", "국내 의류산업 현황 분석 및 분석 앱 개발"),
        Page("pages/4_apartment_AI.py", "AI 기반 맞춤형 아파트 분석 추천시스템"),
        Page("pages/5_ACT.py", "예측모델링 알고리즘을 활용한 종합 적응적 인지검사 시스템 ACT 개발"),
    ]
)

add_page_title()

tab1, tab2 = st.tabs(['소개 및 기술스택', '경력 및 그 외 정보'])

#%% 소개 및 스킬
main_stack = """
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
    <th>구분</th>
    <th>Skill</th>
  </tr>
  <tr>
    <td>Programing Language</td>
    <td>Python, R</td>
  </tr>
  <tr>
    <td>Framework/Library</td>
    <td>1. 데이터분석 : pandas, numpy <br> 2. 데이터 시각화 : matplotlib, seaborn, plotly <br> 3. 머신러닝 : scikit-Learn, catboost, pytorch <br> 4. 추천시스템 : surprise, LightFM, LibRecommender <br> 5. 프론트엔드 : Streamlit, RShiny <br> 6. 백엔드 : FastAPI <br> 7. DB조작 : sqlalchemy, alembic</td>
  </tr>
  <tr>
    <td>BI Tool</td>
    <td>Tableau, Power BI</td>
  </tr>
</table>
"""

sub_stack = """
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
    <th>구분</th>
    <th>Skill</th>
  </tr>
  <tr>
    <td>Deploy</td>
    <td>AWS EC2, AWS Lambda, Cloudtype</td>
  </tr>
  <tr>
    <td>ETC</td>
    <td>GitHub, Docker</td>
  </tr>
</table>
"""

with tab1 : 
    col1, col2, _, col3 = st.columns([2,3,1,4])
    
    with col1 : 
        st.image('src/photo1.jpg', width = 130)
    
    with col2 : 
        st.subheader('윤정한')
        st.write('Data Analyst')
        st.write('Backend Developer')
    
    with col3 :
        st.write('생년월일 : 1994.01.18')
        st.write('Email : wjdgks1999@naver.com')
        st.write('주소 : 경기도 파주시 문산읍')
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('메인 기술스택(Skill Set)')
    st.markdown(main_stack, unsafe_allow_html=True)
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('서브 기술스택(Skill Set)')
    st.markdown(sub_stack, unsafe_allow_html=True)

#%% 경력 및 그 외 정보

career = """
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
    <th>회사명(소재지)</th>
    <th>(주)코리아리서치인터내셔널/서울</th>
    <th>근무기간</th>
    <th>2022.06 ~ 2023.07 <br> 1년 1개월</th>
  </tr>
  <tr>
    <td>부서 및 직위</td>
    <td colspan="3">AI빅데이터사업부/컨설턴트</td>
  </tr>
  <tr>
    <td>회사정보</td>
    <td colspan="3">- 회사규모 : 중소기업 <br> - 매출액 : 200억(22년 기준) <br> - 주요사업 : 시장조사 및 여론조사 <br> 직원수 : 79명</td>
  </tr>
</table>
"""

with tab2 :
    st.subheader('경력 기술서')
    st.markdown(career, unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px dashed #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    st.markdown("""
                ##### Ⅰ. 담당업무
                - 사업계획서 및 발표자료 작성
                - PM(Project Manager) 역할 수행
                - 데이터 수집 : OpenAPI, 웹스크래핑
                - 데이터 분석 : R, Python 활용
                - 데이터 시각화 : RShiny, Power BI 활용
                
                
                ##### Ⅱ. 업무성과
                - AI바우처 사업 수주 및 PM역할 수행을 통한 리서치 정성데이터 AI솔루션 개발 : 사업비 3억원의 프로젝트
                - 데이터바우처 사업 수주 프로젝트 수행 및 완료 : 사업비 7천만원의 프로젝트 종료
                - 데이터바우처 사업 프로젝트 수주 : 사업비 6천만원 프로젝트 수주에 기여
                """)
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('참여 프로젝트')
    
    with st.expander("제주도 여행지 추천 웹서비스 개발(2023.09 ~ 진행중)") :
        st.markdown("- 구분 : 개인 프로젝트")
        st.markdown("- 참여기간 : 2023.09 ~ 진행중")
        st.markdown("- 프로젝트 요약 : AI 기반 개인 맞춤형 제주도 여행지 추천 웹서비스 개발")
        st.markdown("""- 담당 업무
    - 데이터 수집
    - 데이터 분석
    - AI기반 추천시스템 개발
    - AI 연동 API 개발
    - API 배포
                    """)
    
    with st.expander("AI 기반 리서치 정성(Qualitative)데이터 분석 플랫폼 구축(2023.01 ~ 2023.07)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2023.01 ~ 2023.07")
        st.markdown("- 프로젝트 요약 : 시장 및 여론조사에서의 정성문항 답변에 대한 자동 라벨링 플랫폼 개발")
        st.markdown("""- 담당 업무
    - 사업계획서 및 발표자료 작성
    - PM(Project Manager) 역할 수행
    - 도메인 및 학습 대상 데이터 선정 
    - 리서치 정성 답변의 학습 라벨링 체계 확립
    - ML 학습 결과 해석 및 피드백
                    """)
    
    with st.expander("국내 의류산업 현황분석 및 분석앱 개발(2022.06 ~ 2022.12)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2022.06 ~ 2022.12")
        st.markdown("- 프로젝트 요약 : 국내 의류사업군 데이터 분석을 통한 국내 의류사업 실태 인사이트 발굴")
        st.markdown("""- 담당 업무
    - 기업 정보 데이터 수집
    - 데이터 분석
    - 데이터 시각화 플랫폼 개발
    - ML을 통한 인사이트 발굴
    - 보고서 작성
                    """)
    
    with st.expander("AI 기반 맞춤형 아파트 분석 추천시스템 개발(2022.06 ~ 2022.12)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2022.06 ~ 2022.12")
        st.markdown("- 프로젝트 요약 : 아파트 부동산 데이터 기반 개인맞춤형 아파트 추천시스템 개발")
        st.markdown("""- 담당 업무
    - 데이터 수집
    - 데이터 분석
    - 데이터 시각화
    - 추천시스템 개발을 위한 선호도 설문지 작성
                    """)

    with st.expander("예측모델링 알고리즘을 활용한 종합 적응적 인지검사 시스템 ACT 개발(2021.10 ~ 2021.12)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2021.10 ~ 2021.12")
        st.markdown("- 프로젝트 요약 : ML을 이용한 기존보다 80% 짧은 길이의 인지검사 시스템 개발")
        st.markdown("""- 담당 업무
    - 데이터 전처리 및 분석
    - ML을 이용한 적응적 검사 개발
    - 결과 보고서 작성
    - Working Technical Document 작성
                    """)
        st.markdown("참조 : http://211.169.249.237/site/defaultMain.do")

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

    st.subheader('학력')
    st.markdown("""
                ##### 1. 중앙대학교 일반대학원(석사)
                - 2019.09 ~ 2022.02(졸업)
                - 전공 : 계량심리학
                - 지역 : 서울
                - 학점 : 4.41/4.5
                - 논문 : [한국심리학회지: 일반]컴퓨터 기반 적응적 심리 검사 제작을 위한 문항 선정 알고리즘으로서 Alternating Model Tree의 활용 가능성 탐색
                    - https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002789781
                
                ##### 2. 중앙대학교(서울)(4년제)
                - 2013.03 ~ 2019.08(졸업)
                - 전공 : 심리학과
                - 학점 : 4.0/4.5
                - 지역 : 서울
                """)