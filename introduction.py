import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

#%%0. 페이지 설정
show_pages(
    [
        Page("introduction.py", "소개", "🏠"),        
        Section(name="참여 프로젝트", icon=":pig:"),
        Page("pages/1_travel_recommend.py", "제주도 관광지 추천 웹서비스 개발", icon=":one:"),
        Page("pages/2_qualitative_AI.py", "AI기반 리서치 정성데이터 분석플램폼 구축", icon=":two:"),
        Page("pages/3_clothes_industry.py", "국내 의류산업 현황 분석 및 분석 앱 개발", icon=":three:"),
        Page("pages/5_ACT.py", "ML을 활용한 종합 적응적 인지검사 시스템 ACT 개발", icon=":four:"),
        Section(name="서브 프로젝트", icon=":pig:"),
        Page("pages/4_apartment_AI.py", "AI 기반 맞춤형 아파트 분석 추천시스템 개발", icon=":one:"),
    ]
)

add_page_title()

tab1, tab2 = st.tabs(['소개 및 기술스택', '경력 및 그 외 정보'])

#%% 1. 테이블 불러오기
@st.cache_data
def load_main_stack() :
  with open("src/introduction/main_stack.html", "r", encoding="utf-8") as file:
      main_stack_code = file.read()
  return main_stack_code

main_stack = load_main_stack()

@st.cache_data
def load_sub_stack() :
  with open("src/introduction/sub_stack.html", "r", encoding="utf-8") as file:
      sub_stack_code = file.read()
  return sub_stack_code

sub_stack = load_sub_stack()

@st.cache_data
def load_career() :
  with open("src/introduction/career.html", "r", encoding="utf-8") as file:
      career_code = file.read()
  return career_code

career = load_career()

#%%2. 소개
with tab1 : 
    col1, col2, _, col3 = st.columns([2,3,1,4])
    
    with col1 : 
        st.image('src/introduction/face.png', width = 130)
    
    with col2 : 
        st.subheader('윤정한')
        st.write('Data Analyst')
    
    with col3 :
        st.write('생년월일 : 1994.01.18')
        st.write('주소 : 경기도 파주시 문산읍')
        st.write('Email : wjdgks1999@naver.com')
        st.write('Phone : 010-2280-1999')
        st.write("GitHub : https://github.com/jhyoon1999")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('메인 기술스택(Skill Set)')
    st.markdown(main_stack, unsafe_allow_html=True)
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('서브 기술스택(Skill Set)')
    st.markdown(sub_stack, unsafe_allow_html=True)

#%% 3. 경력
with tab2 :
    st.subheader('경력')
    st.markdown(career, unsafe_allow_html=True)
    st.markdown('<hr style="border: 0.5px dashed #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    with st.expander("담당업무 및 업무성과") :
      st.markdown("""##### Ⅰ. 담당업무""")
      st.write("""
              1. 사업계획서 및 발표자료 작성
              - 효과적인 사업전략을 수립하고 이를 기반으로 사업계획서 작성 및 발표자료 제작.
              - 주요 이니셔티브 및 비전을 명확히 전달하여 이해를 도모.
              """)
      st.text("\n")
      st.write("""
              2. 데이터 수집
              - 다양한 소스로부터 데이터를 수집하고, 정확한 데이터 수집 계획 수립.
              - 데이터 수집 프로세스 개선을 통한 효율적이고 신뢰성 있는 데이터 획득.
              """)
      st.text("\n")
      st.write("""
              3. 데이터 분석/시각화
              - 통계 및 머신러닝 기법을 활용하여 데이터를 분석하고 인사이트 도출.
              - 시각화 도구를 활용하여 결과물을 명확하게 시각화하고 이해하기 쉽게 전달.
              """)
      st.text("\n")
      st.write("""
              4. 대시보드/BI Report 개발 및 운영
              - 업무 수행에 필요한 대시보드 및 BI Report를 개발하고 유지보수.
              - 실시간 데이터 모니터링을 통한 의사결정 지원.
              """)
      st.text("\n")
      st.write("""
              5. 문서 작업
              - 업무 프로세스 등과 관련된 문서 작성.
              - 프로젝트 진행에 필요한 문서 작업 및 보고서 작성.
              """)
      st.text("\n")
      st.markdown("""##### Ⅱ. 업무성과""")
      st.write("""
              1. AI바우처 사업 수주 및 PM역할 수행을 통한 리서치 정성데이터 AI솔루션 개발
              - 3억원 규모의 사업 수주 성공 및 PM으로서 프로젝트 수행.
              - 리서치 정성데이터 AI 솔루션 개발을 통해 기업의 효율성 향상에 기여.
              """)
      st.text("\n")
      st.write("""
              2. 데이터바우처 사업 수주 프로젝트 수행 및 완료
              - 7천만원 규모의 프로젝트를 성공적으로 완료하며 고객 만족 달성.
              - 프로젝트 종료 후에도 지속적인 관리와 유지보수로 고객 신뢰 확보.
              """)
      st.text("\n")
      st.write("""
              3. 데이터바우처 사업 프로젝트 수주 성공
              - 6천만원 규모의 사업비로 프로젝트 수주를 이끌어내어 기업의 수익성 향상에 기여.
              - 프로젝트 수행을 위한 효율적이고 체계적인 계획 수립으로 성과 창출.
              """)

    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader('참여 프로젝트')
    
    with st.expander("제주도 관광지 추천 웹서비스 개발") :
        st.markdown("- 구분 : 개인 프로젝트")
        st.markdown("- 참여기간 : 2023.09 ~ 2023.11 (3개월)")
        st.markdown("- 프로젝트 요약 : AI 기반 개인 맞춤형 제주도 관광지 추천 웹서비스 개발")
        st.markdown("- 담당 업무 : 데이터 수집, 데이터 분석, AI기반 추천시스템 개발, API 개발")
        st.markdown("- 성과 : 최소기능제품(https://jejuai.web.app/#/) 개발 완료")
        st.markdown("- 기술 : MySQL, Python, FastAPI, AWS")
    
    with st.expander("AI 기반 리서치 정성(Qualitative)데이터 분석 플랫폼 구축") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2023.04 ~ 2023.07 (4개월)")
        st.markdown("- 프로젝트 요약 : 시장 및 여론조사에서의 정성문항 답변에 대한 자동 라벨링 플랫폼 개발")
        st.markdown("- 담당업무 : 사업계획서 및 발표자료 작성, 도메인 및 학습 대상 데이터 선정 및 대시보드 운영, 학습 라벨링 체계 확립")
        st.markdown("- 성과 : 사업비 3억원 사업 수주 성공, 학습 대상 데이터 선정 완료, 학습 대상 통합 라벨링 체계 확립 완료")
        st.markdown("- 기술 : MySQL, Python, Power BI")
    
    with st.expander("국내 의류산업 현황분석 및 분석앱 개발") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2022.06 ~ 2022.12 (6개월)")
        st.markdown("- 프로젝트 요약 : 국내 의류사업군 데이터 분석을 통한 국내 의류사업 실태 인사이트 발굴")
        st.markdown("- 담당업무 : 기업 정보 데이터 수집/석, 데이터 분석앱 개발, 인사이트 도출 및 보고서 작성")
        st.markdown("- 성과 : 데이터 분석앱 개발 완료, 사업비 7천만원 프로젝트 수행 완료")
        st.markdown("- 기술 : R, Shiny")

    with st.expander("ML을 활용한 종합 적응적 인지검사 시스템 ACT 개발") :
        st.markdown("- 구분 : 팀 프로젝트")
        st.markdown("- 참여기간 : 2021.10 ~ 2021.12 (3개월)")
        st.markdown("- 프로젝트 요약 : ML을 이용한 기존보다 80% 짧은 길이의 인지검사 시스템 개발")
        st.markdown("- 담당업무 : 데이터 가공/분석, ML을 이용한 적응적 검사 개발, 결과 보고서/Working Technical Document 작성")
        st.markdown("- 성과 : 적응적 인지능력 검사 시스템 ACT 개발 및 런칭 성공(http://211.169.249.237/site/defaultMain.do)")
        st.markdown("- 기술 : R")
        

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