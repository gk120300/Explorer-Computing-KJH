import streamlit as st

st.set_page_config(
    page_title="나의 포트폴리오",
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

st.info("Ex ch10 p1: 자기소개서")
st.success("Ex ch10 p2: 수업시간표")

st.markdown("---")
st.caption("2025 Made with Streamlit")
