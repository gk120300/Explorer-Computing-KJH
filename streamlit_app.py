import streamlit as st

st.set_page_config(
    page_title="김지후 포트폴리오",
    page_icon="📚",
    layout="wide"
)

st.title("포트폴리오 사이트")
st.markdown("---")

st.header("환영합니다")

st.write("""
이 사이트는 제 과제를 모아놓은 포트폴리오입니다.

왼쪽 사이드바에서 보고 싶은 페이지를 선택해주세요.
""")

col1, col2 = st.columns(2)

with col1:
    st.info("p1: 자기소개서")
    st.write("나에 대한 소개와 관심사")
    
with col2:
    st.success("p2: 수업시간표")
    st.write("이번 학기 수업 시간표")

st.markdown("---")

st.subheader("컴퓨팅 탐색")
st.write("Python과 Streamlit을 활용한 웹 애플리케이션")

st.markdown("---")
st.caption("2025 Made with Streamlit")
