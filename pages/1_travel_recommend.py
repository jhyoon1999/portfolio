import streamlit as st
from st_pages import add_page_title

add_page_title(layout = "wide")

tab1, tab2, tab3 = st.tabs(["요약", "프로젝트 진행", "코드"])

#%% 1. 요약

travel_summary = """
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
    <td>2023.09 ~ 2023.11</td> 
  </tr>
  <tr>
    <th>프로젝트 내용</th>
    <td colspan="2">취향, 연령, 성별 등의 개인적 특성에 기반한 제주도 여행지 추천 웹서비스 개발</td> 
  </tr>
  <tr>
    <th>사용언어/프레임워크</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/python_logo.png" alt="Python Image" width="80" height="50">
      <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/fastapi_logo.png" alt="FastAPI Image" width="80" height="50">
    </td>
  </tr>
  <tr>
    <th>데이터베이스</th>
    <td>
      <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/Mysql_logo.png" alt="MySQL Image" width="80" height="50">
    </td>
  </tr>
</table>
"""

with tab1 :
    subcol1, subcol2 = st.columns([7,3])
    with subcol1 :
        st.subheader("Ⅰ. 프로젝트 요약")
        st.markdown(travel_summary, unsafe_allow_html=True)
    with subcol2 :
        st.text("\n")
        st.text("\n")
        st.write("###### 담당업무(기여도)")
        st.progress(value=100, text = "데이터 수집/가공(100%)")
        st.progress(value=100, text = "분석/시각화(100%)")
        st.progress(value=100, text = "추천시스템 개발(100%)")
        st.progress(value=100, text = "API 개발(100%)")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅱ. WBS")
    st.image("https://raw.githubusercontent.com/jhyoon1999/image_logo/master/travel_recommend/WBS_recommend.png", use_column_width="auto")
    
    st.markdown('<hr style="border: 1px solid #ccc; margin: 20px 0;">', unsafe_allow_html=True)
    
    st.subheader("Ⅲ. 결과물")
    with st.expander("01)API Documnet") :
        st.components.v1.html('<iframe src="https://o5as6un2knzd5sl6ldr2gnn3ba0mbgdy.lambda-url.ap-northeast-2.on.aws/docs#/" width="800" height="600"></iframe>', height=600)
    with st.expander("02)최소기능제품") :
        st.components.v1.html('<iframe src="https://jejuai.web.app/#/" width="900" height="600"></iframe>', height=600)

#%%2. 프로젝트 진행
algorithms_info = """
<style>
    table {
        width:100%;
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
    <th>선정 여부</th>
  </tr>
  <tr>
    <td>Hybrid Approach</td>
    <td>LightFM</td>
    <td>Content-based와 Collaborative Filtering의 장점을 결합한 Hybrid 알고리즘</td>
    <td>X</td>
  </tr>
  <tr>
    <td>DeepFM</td>
    <td>LibRecommender</td>
    <td>FM(Factorization Machine)과 딥러닝(DNN)을 결합시킨 알고리즘</td>
    <td>X</td>
  </tr>
  <tr>
    <td>CatBoost</td>
    <td>CatBoost</td>
    <td>의사결정나무(Decision-Tree) 기반 ensemble method 중 하나로 범주형 변수에 대한 효율적인 처리를 장점으로 갖는 알고리즘</td>
    <td>O</td>
  </tr>
</table>
"""

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
            st.markdown(f'<div style="border: 2px solid {"orange"}; padding: 10px; max-width:800px;">\
                    <div style="position:relative; text-align:left;">\
                        <p style="font-weight:normal;">{"〮자료출처 : AI-Hub 국내 여행로그 데이터(제주도 및 도서지역)"}</p>\
                        <p style="font-weight:normal;">{"〮핵심 데이터 테이블 선정 → 데이터 모델링 후 Raw Data 적재 및 관리"}</p>\
                    </div>\
                    <div style="position:relative; text-align:center;">\
                        <img src="{"https://raw.githubusercontent.com/jhyoon1999/image_logo/master/travel_recommend/important_table.png"}" alt="image" style="max-width:100%; max-height:400px;">\
                    </div>\
                    <div style="position:relative; text-align:left;">\
                        <p style="font-weight:normal;">{"〮데이터 정제 프로세스"}</p>\
                    </div>\
                    <div style="position:relative; text-align:center;">\
                        <img src="{"https://raw.githubusercontent.com/jhyoon1999/image_logo/master/travel_recommend/preprocessing.png"}" alt="image" style="max-width:100%; max-height:400px;">\
                    </div>\
                </div>', unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(2). 분석/시각화
    scol1, scol2 = st.columns([2,8])
    with scol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"분석/시각화"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with scol2 :
            st.markdown(f'<div style="border: 2px solid {"orange"}; padding: 10px; max-width:800px;">\
                    <div style="position:relative; text-align:left;">\
                        <p style="font-weight:normal;">{"〮여행객/관광지 특성 기반 클러스터링 실시 → 클러스터링 결과를 예측변수로 활용"}</p>\
                        <p style="font-weight:normal;">{"〮60여개의 변수 중 여행객의 관광지 방문만족도를 설명하는 주요 변수 추출→ 만족도 예측변수로 활용"}</p>\
                    </div>\
                    <div style="position:relative; text-align:center;">\
                        <img src="{"https://raw.githubusercontent.com/jhyoon1999/image_logo/master/travel_recommend/analysis.png"}" alt="image" style="max-width:100%; max-height:400px;">\
                    </div>\
                </div>', unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

    #(3). 추천시스템 개발
    tcol1, tcol2 = st.columns([2,8])
    with tcol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"추천시스템 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with tcol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">\
                <div style="position:relative; text-align:left;">\
                    <p style="font-weight:normal;">{"〮알고리즘 후보군 선정"}</p>\
                </div>\
                <div style="position:relative; text-align:center;">\
                    {algorithms_info}\
                </div>\
                <div>\
                    <div style="position:relative; text-align:left;">\
                        <p style="font-weight:normal;">{"〮모델 성능(만족도 범위 : 1-5점)"}</p>\
                    </div>\
                    <div style="position:relative; text-align:center;">\
                        <img src="https://raw.githubusercontent.com/jhyoon1999/image_logo/master/travel_recommend/performance_AI.png" alt="image" style="max-width:100%; max-height:400px;">\
                    </div>\
                </div>\
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)
    
    #(4). API 개발
    focol1, focol2 = st.columns([2,8])
    with focol1 :
        st.markdown(f'<div style="position:relative;">\
                            <div style="border: 2px solid {"grey"}; padding: 10px; display: inline-block;">\
                                <span style="font-weight:bold;">{"API 개발"}</span>\
                            </div>\
                        </div>', unsafe_allow_html=True)
    with focol2 :
        st.markdown(f"""
            <div style="border: 2px solid orange; padding: 10px; max-width:800px;">\
                <div style="position:relative; text-align:left;">\
                    <p style="font-weight:normal;">{"〮개발프레임워크 : FastAPI"}</p>\
                    <p style="font-weight:normal;">{"〮배포 : AWS"}</p>\
                    <p style="font-weight:normal;">{"〮메소드 : POST"}</p>\
                    <p style="font-weight:normal;">{"〮Request Body : 유저특성(User Features)"}</p>\
                    <p style="font-weight:normal;">{"〮요청결과 : 각 카테고리 별 관광지 5곳"}</p>\
                </div>\
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown('<hr style="border: 0.5px solid orange; margin: 20px 0;">', unsafe_allow_html=True)

#%% 3. 코드
with open("src/travel_recommend/lightfm_code.py", 'r', encoding='utf-8') as lightfm_read :
    lightfm_code = lightfm_read.read()

with open("src/travel_recommend/deepfm_code.py", 'r', encoding='utf-8') as deepfm_read :
    deepfm_code = deepfm_read.read()

with open("src/travel_recommend/catboost_code.py", 'r', encoding='utf-8') as catboost_read :
    catboost_code = catboost_read.read()

with tab3 :
    with st.expander("LightFM 모델링 코드") :
        st.code(lightfm_code, language = "python")
    
    with st.expander("DeepFM 모델링 코드") :
        st.code(deepfm_code, language = "python")
    
    with st.expander("CatBoost 모델링 코드") :
        st.code(catboost_code, language = "python")
    
    with st.expander("FastAPI 코드") :
        st.link_button("github 바로가기", url = "https://github.com/jhyoon1999/recommend_api/blob/master/")