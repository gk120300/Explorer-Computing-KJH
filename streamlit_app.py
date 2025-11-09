import streamlit as st
import pandas as pd
import numpy as np

# Streamlit 설정 (가장 위에 있어야 함)
st.set_page_config(
    page_title="김지후 학생의 과제 앱",
    page_icon="👋",
)

st.title("김지후 학생의 Streamlit 과제 제출 앱 👋")
st.write("---")

# 메인 페이지 내용 (사용자님의 예제 코드)
st.header("간단한 Streamlit 예제")
st.write("이 페이지는 앱의 메인 화면이며, 데이터와 그래프를 보여주는 예제입니다.")

# 샘플 데이터 생성
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.dataframe(data)
st.line_chart(data)

# 사이드바 안내
st.sidebar.success("왼쪽 메뉴에서 과제 페이지를 선택해 주세요.")

st.markdown("""
### 페이지 구성 안내
**👈 왼쪽 메뉴에서 다음 페이지로 이동하세요:**
* **1 자기소개:** 첫 번째 과제
* **2 시간표:** 두 번째 과제
""")
