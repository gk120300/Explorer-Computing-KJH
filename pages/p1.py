import streamlit as st
import pandas as pd

st.markdown("# 나의 소개 페이지")

st.markdown("## 자기소개")
st.markdown(f"""
안녕하세요, 제 이름은 **김지후**입니다.
산림과학부에 재학중이고, 현재 2학년입니다.
GUI 구성에 관심이 많았어요.
""")

st.write({"이름": "김지후", "나이": 21})

st.markdown("## 좋아하는 것")
st.markdown(f"""
저는 독서와 산책을 좋아합니다. 산에도 가끔 가고요.
노래는 듣는 것을 좋아하며, 가장 좋아하는 노래는 아래 링크입니다.
""")
st.markdown("[the brilliant green-holidays!](https://www.youtube.com/watch?v=PRa1MheycR4)")

st.markdown("## 앞으로의 목표")
st.markdown("데이터 분석이 낯설어서 열심히 해보겠습니다.")

st.caption("가장 좋아하는 코드?...")
st.code("messagebox.askyesno()", language="python")
st.markdown("이 기능이 제일 매력적이에요.")

st.caption("생각나는 공식?...")
st.markdown("깁스 자유 에너지")
st.latex(r"G=U+PV-TS")
