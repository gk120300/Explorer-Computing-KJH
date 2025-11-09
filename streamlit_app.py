import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="김지후"
)

st.title("김지후 컴탐실 과제 제출 ")
st.write("---")

# 사이드바 안내
st.sidebar.header("Sidebar Menu")

st.title("컴퓨팅 탐색")          
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Ex_ch10_p1")
    st.write("자기소개")
    
with col2:
    st.subheader("📄 Ex_ch10_p2")
    st.write("시간표")

