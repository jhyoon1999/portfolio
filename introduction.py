import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

show_pages(
    [
        Page("introduction.py", "소개", "🏠"),        
        Section(name="참여 프로젝트", icon=":pig:"),
        Page("pages/1_travel_recommend.py", "제주도 여행지 추천 웹서비스 개발"),
        Page("pages/2_qualitative_AI.py", "AI기반 리서치 정성데이터 분석플램폼 구축"),
        Page("pages/3_clothes_industry.py", "기존 제작 대비 저렴한 공동생산방식의 의류제작 플랫폼"),
        Page("pages/4_apartment_AI.py", "AI 기반 맞춤형 아파트 분석 추천시스템"),
        Page("pages/5_ACT.py", "예측모델링 알고리즘을 활용한 종합 적응적 인지검사 시스템 ACT 개발"),
    ]
)

add_page_title()

tab1, tab2, tab3 = st.tabs(['소개 및 기술스택', '경력 및 그 외 정보', '자기소개'])

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
    <td>1. 데이터분석 : pandas, numpy <br> 2. 데이터 시각화 : matplotlib, seaborn, plotly <br> 3. 머신러닝 : scikit-Learn, catbbost pytorch <br> 4. 추천시스템 : surprise, LightFM, LibRecommender <br> 5. 프론트엔드 : Streamlit, Shiny <br> 6. 백엔드 : fastapi <br> 7. DB : sqlalchemy, alembic</td>
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
    <td>AI빅데이터사업부/컨설턴트</td>
    <td>연봉</td>
    <td>3740만원</td>
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
                - 데이터 분석 시각화 : RShiny, Power BI 활용
                
                
                ##### Ⅱ. 업무성과
                - AI바우처 사업 수주 및 PM역할 수행을 통한 리서치 NLP AI솔루션 개발 : 사업비 3억원의 프로젝트
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
    - API 개발
    - 배포
                    """)
    
    with st.expander("AI 기반 리서치 정성(Qualitative)데이터 분석 플랫폼 구축(2023.01 ~ 2023.07)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2023.01 ~ 2023.07")
        st.markdown("- 프로젝트 요약 : 시장 및 여론조사에서의 텍스트 답변에 대한 자동 라벨링 플랫폼 개발")
        st.markdown("""- 담당 업무
    - 사업계획서 및 발표자료 작성
    - PM(Project Manager) 역할 수행
    - 도메인 및 학습 대상 데이터 선정 
    - 리서치 정성 답변의 학습 라벨링 체계 확립
    - ML 학습 결과 해석 및 피드백
                    """)
    
    with st.expander("기존 제작 대비 30% 저렴한 공동생산 방식의 의류제작 플랫폼 개발(2022.06 ~ 2022.12)") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2022.06 ~ 2022.12")
        st.markdown("- 프로젝트 요약 : 국내 의류사업군 데이터 분석을 통한 국내 의류사업 실태 인사이트 발굴")
        st.markdown("""- 담당 업무
    - 기업 정보 데이터 수집
    - 데이터 분석
    - 데이터 시각화 플랫폼 개발
    - ML을 통한 인사이트 발굴
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

#%% 자기소개서
with tab3 :
    
    st.markdown("##### 1. 성장과정")
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    growth = """
    저는 부족하지 않은 환경에서 자랐습니다. 
    물론 물질적으로 타인에 비해 풍족하다고는 할 수 없었으나 부모님께서는 항상 삶의 여유를 가지면서 사시려고 노력하셨습니다. 
    그렇다보니 저도 삶에서 여유를 가지고 살기 위해 노력했습니다. 이러한 저의 태도는 타인을 대할 때 두드러졌습니다. 
    타인과 업무 및 사적인 대화를 할 때 타인의 가치관, 생각, 행동이 나와는 다를 수 있고, 이는 옳고 그름이 아니라 시각의 다름임을 항상 인지하려고 노력합니다.
    이는 데이터 분석 및 인사이트 발견에 있어서 매우 중요하다고 생각합니다. 동일한 차트를 보고 타인은 다른 해석을 할 수 있으며, 색다른 시각은 본인의 생각에만 갇히지 않게끔 해줍니다.
    따라서 저는 다양한 의견을 취합하여 더 나은 인사이트와 의사결정을 내리기 위해 커뮤니케이션 하려고 노력하며, 저의 태도가 데이터 분석에서 가장 중요한 자질이라고 생각합니다.
        """
    
    container_with_border1 = f"""
    <div style="
        border: 2px solid #000; /* 테두리 스타일 및 색상 설정 */
        padding: 0px; /* 컨테이너 내부 여백 설정 */
    ">
    {growth}
    </div>
    """
    
    st.markdown(container_with_border1, unsafe_allow_html=True)
    
    empty_space = '<div style="height: 30px;"></div>'
    st.markdown(empty_space, unsafe_allow_html=True)

    st.markdown("##### 2. 성격소개 (장점/단점, 취미/특기, 생활신조 등)")
    
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    character = """
    저의 가장 큰 장점은 도전정신과 이에 따른 적극성입니다. 
    제가 맡는 업무를 누구보다 완벽히 수행하기 위해 시간을 쪼개서 필사적으로 노력하며, 부족한 역량이 발견되면 밤을 세서라도 이를 갖추기 위해 노력합니다. 
    하지만 이러한 장점이 너무 과하여, 업무 후에 쉽게 지치는 체력적인 단점을 갖고 있습니다. 해당 단점을 극복하기 위해 운동을 통해 체력을 기르고, 명상을 통해 스트레스를 관리하는 취미를 갖고 있습니다.
    """
    
    container_with_border2 = f"""
    <div style="
        border: 2px solid #000; /* 테두리 스타일 및 색상 설정 */
        padding: 0px; /* 컨테이너 내부 여백 설정 */
    ">
    {character}
    </div>
    """
    
    st.markdown(container_with_border2, unsafe_allow_html=True)

    st.markdown(empty_space, unsafe_allow_html=True)
    
    st.markdown("##### 3. 희망업무 및 업무상 강점")
    
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    work = """
    저의 업무상 강점은 다음의 세 가지 역량 및 경험으로 요약할 수 있으며, 이와 같은 업무능력을 바탕으로 데이터분석 포지션에 지원하고자 합니다.

    1. 빅데이터 분석 능력
    ⋅다양한 업종(의류산업, 부동산, 인지능력검사, 마케팅 리서치)의 데이터에 대한 분석 경험
    ⋅데이터 분석 기반 인사이트 제공 경험

    2. 다양한 프로그래밍 언어 활용 능력
    ⋅R, Python 등의 데이터사이언스 언어 활용 가능
    ⋅Tableau, Power BI 등 BI솔루션 활용 가능
    ⋅그 외 업무에 필요한 프로그램(SQL, Exel) 활용 가능

    3. 빅데이터 프로젝트 PM 능력
    ⋅AI바우처, 데이터바우처 사업 수주 프로젝트에서 PM으로써 프로젝트 운영 및 완수 경험

    4. 머신러닝 기반 AI 솔루션 개발 능력
    ⋅채용 목적의 AI기반 인지능력 검사 개발 경험

    """
    
    container_with_border3 = f"""
    <div style="
        border: 2px solid #000; /* 테두리 스타일 및 색상 설정 */
        padding: 0px; /* 컨테이너 내부 여백 설정 */
    ">
    {work}
    </div>
    """
    
    st.markdown(container_with_border3, unsafe_allow_html=True)

    st.markdown(empty_space, unsafe_allow_html=True)

















