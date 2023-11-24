import streamlit as st
from st_pages import add_page_title
from streamlit_mermaid import st_mermaid

add_page_title(layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["개요", "WBS", "프로젝트 진행",
                                "기타"])

#%% 개요

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

with tab1 :
    st.subheader("Ⅰ. 프로젝트 개요")
    
    st.markdown("- 프로젝트명 : 제주도 여행지 추천 웹서비스 개발")
    
    st.markdown('- 프로젝트 기간 : 2023.09 ~ 진행중')
    
    st.markdown("- 고객 니즈(인터뷰)")
    interview = st.button(label = "펼치기:sunglasses:", key = "interview", on_click= click_button)
    
    if st.session_state.button :
        st.image("src/travel_recommend/needs_recommend.png", use_column_width = "auto")
        
    st.markdown("- 프로젝트 내용 : 취향, 연령, 여행 주제 등의 개인적 특성에 기반한 제주도 여행지 추천 웹서비스 개발")
    st.markdown("""
                - 주요 언어
                    - 데이터 분석 및 머신러닝 : python
                    - 백엔드 개발 : python
                    - 프론트엔드 개발 : Flutter
                """)
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. 담당업무")
    st.markdown("""
                - 데이터 수집 및 분석
                - AI 기반 추천시스템 개발
                - AI 연동 API 개발
                """)
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)

#%% WBS

with tab2 :
    st.image("src/travel_recommend/WBS_recommend.png")

#%% 프로젝트 진행

cleaning_process = """
    classDiagram
        여행 --|> USER_FEATURES : Aggregation
        여행객Master --|> USER_FEATURES : Aggregation
        방문지 --|> ITEM_RATINGS : Filtering
        방문지  --|> Not_Searched_SPOT : Filtering
        방문지  --|> Not_JEJU : Filtering
        USER_FEATURES --|> Cleaning Data : Aggregation
        ITEM_RATINGS --|> Cleaning Data : Aggregation
        Cleaning Data --|> 추천대상선정 : Filtering
        추천대상선정 --|> Train Data : Filtering
        
        class 여행
        여행 : -주요변수-
        여행 : 1. 여행ID
        여행 : 2. 여행객ID
        여행 : 3. 여행미션
        
        여행 : (구성)
        여행 : (3600개의 개별적인 여행 SET)
        
        class 여행객Master
        여행객Master : -주요변수-
        여행객Master : 1. 여행객ID
        여행객Master : 2. 성별
        여행객Master : 3. 연령대
        여행객Master : 4. 여행스타일
        여행객Master : 5. 여행동기
        여행객Master : 6. 동반현황
        
        여행객Master : (구성)
        여행객Master : (3600개의 개별적인 여행 SET)
        
        class 방문지
        방문지 : -주요변수-
        방문지 : 1. 여행ID
        방문지 : 2. 방문지명
        방문지 : 3. 체류시간
        방문지 : 4. 방문지유형코드
        방문지 : 5. 방문석택이유
        방문지 : 6. 만족도
        방문지 : 7. 재방문의향
        방문지 : 8. 추천의향
        
        방문지 : (구성)
        방문지 : (4243개 여행방문지 SET)
        
        class USER_FEATURES
        USER_FEATURES : 여행정보와 여행객MASTER 정보를 모두 갖는 3238개 여행 SET
        
        class ITEM_RATINGS
        ITEM_RATINGS : 카카오지도에서 검색된 제주도 방문지 2315개
        
        class Not_Searched_SPOT
        Not_Searched_SPOT : 카카오지도에서 검색되지 않은 방문지 365개
        
        class Not_JEJU 
        Not_JEJU : 제주도가 아닌 방문지 1563개
        
        class Cleaning Data
        Cleaning Data : USER_FEATURES과 ITEM_RATINGS를 join한 데이터
        Cleaning Data : (구성)
        Cleaning Data : (1. 2504개 TRAVEL_ID)
        Cleaning Data : (2. 2004개의 SPOT_ID --> 통합과정을 통한 New Spot_ID 1684개)
        Cleaning Data : (3. 13540개의 RATING)
        
        class 추천대상선정
        추천대상선정 : 카카오지도 API 업종 분류
        추천대상선정 : 1. 여행
        추천대상선정 : 2. 스포츠, 레저
        추천대상선정 : 3. 음식점 > 카페
        추천대상선정 : 4. 서비스, 산업
        추천대상선정 : 5. 문화, 예술
        추천대상선정 : 6. 가정, 생활 > 시장
        추천대상선정 : 7. 교통, 수송
        
        class Train Data
        Train Data : 여행지 1318곳
        Train Data : 여행객 2457명
        Train Data : rating 12587개
    """

algorithms_info = """
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
    <th>알고리즘</th>
    <th>라이브러리</th>
    <th>설명</th>
  </tr>
  <tr>
    <td>Hybrid Approach</td>
    <td>LightFM</td>
    <td>Content-based와 Collaborative Filtering의 장점을 결합한 Hybrid 알고리즘</td>
  </tr>
  <tr>
    <td>DeepFM</td>
    <td>LibRecommender</td>
    <td>FM(Factorization Machine)과 딥러닝(DNN)을 결합시킨 알고리즘</td>
  </tr>
  <tr>
    <td>CatBoost</td>
    <td>CatBoost</td>
    <td>의사결정나무(Decision-Tree) 기반 ensemble method 중 하나로 범주형 변수에 대한 효율적인 처리를 장점으로 갖는 알고리즘</td>
  </tr>
</table>
"""

with tab3 :
    col1, arrow1, col2, arrow2, col3, arrow3, col4 = st.columns(7)
    
    with col1 :
        f = st.button(label = "데이터 수집", key = "first", type="primary")
    
    with arrow1 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    
    with col2 :
        s = st.button(label = "데이터 정제", key = "second",type="primary")
    
    with arrow2 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    
    with col3 : 
        t = st.button(label = "AI 기반 추천시스템 설계", key = "third", type="primary")
    
    with arrow3 :
        st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    
    with col4 :
        fo = st.button(label = "AI 연동 API 개발", key = "fourth", type="primary")
    
    
    if f :
        st.markdown("""
                    -  데이터 수집
                        - 데이터 출처 : AI-Hub
                        - 데이터 url : https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71584
                        - 데이터 ERD
                    """)
        st.image("src/travel_recommend/ERD_recommend.png")
        
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 핵심 데이터 테이블 선택
                    """)
        
        column1, column2, column3 = st.columns(3)
        
        with column1 :
            st.image("src/travel_recommend/table1.png")
        
        with column2 :
            st.image("src/travel_recommend/table2.png")
        
        with column3 :
            st.image("src/travel_recommend/table3.png")
    
    if s :
        st.markdown("""
                    - 데이터 정제 프로세스
                    """)
        
        st_mermaid(cleaning_process, height= "500px")
        
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 주요변수 정의
                        - catboost 기반 만족도 예측에서의 변수중요도(variable importance) 산출
                        - 중요 변수들은 추후 추천시스템에서 예측변수로 활용
                    """)
        st.image("src/travel_recommend/variable_importance_recommend.png")
        
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("- 데이터 시각화")
        st.image("src/travel_recommend/data_vis.png")
    
    if t :
        st.markdown("""
                    - 목표 : 유저 특성(user features)과 방문지 특성(item features)을 이용해 서비스 이용자의 방문지에 대한 만족도를 예측하는 AI 개발
                    - 알고리즘 후보군 선정
                    """)
        st.markdown(algorithms_info, unsafe_allow_html=True)
        
        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        
        st.markdown("""
                    - 선정 : CatBoost
                    - 선정사유 
                        - 일반적인 추천시스템 알고리즘은 추천을 위해 사용자와 아이템의 실제 상호작용을 요구
                        - CatBoost는 예측변수(유저특성, 방문지특성) 값만으로 예측이 가능함
                        - CatBoost는 범주형 특성이 많을 경우 높은 예측성능을 보임 
                    """)

        st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
        st.markdown("- 모델성능")
        _, performance_column, _ = st.columns([1,8,1])
        with performance_column :
            st.image("src/travel_recommend/performance_AI.png")
    
    if fo :
        st.markdown("""
                    - 목표 : 유저특성(user features)을 Request Body로 한 POST 요청시 각 카테고리 별로 높은 예측점수를 보인 관광지 5곳을 추천해주는 API 개발
                    - 프레임워크 : FastAPI
                    - 배포 : AWS ECR, AWS Lambda
                    - API Documnet
                    """)
        st.components.v1.html('<iframe src="https://o5as6un2knzd5sl6ldr2gnn3ba0mbgdy.lambda-url.ap-northeast-2.on.aws/docs/" width="1500" height="600"></iframe>', height=600)

#%% 기타

with open("src/travel_recommend/lightfm_code.py", 'r', encoding='utf-8') as lightfm_read :
    lightfm_code = lightfm_read.read()

with open("src/travel_recommend/deepfm_code.py", 'r', encoding='utf-8') as deepfm_read :
    deepfm_code = deepfm_read.read()

with open("src/travel_recommend/catboost_code.py", 'r', encoding='utf-8') as catboost_read :
    catboost_code = catboost_read.read()

with tab4 :
    with st.expander("LightFM 모델링 코드") :
        st.code(lightfm_code, language = "python")
    
    with st.expander("DeepFM 모델링 코드") :
        st.code(deepfm_code, language = "python")
    
    with st.expander("CatBoost 모델링 코드") :
        st.code(catboost_code, language = "python")
    
    with st.expander("FastAPI 코드") :
        st.link_button("github 바로가기", url = "https://github.com/jhyoon1999/recommend_api/blob/master/")