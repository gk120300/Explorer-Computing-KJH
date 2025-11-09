# 여기에 코드를 작성해주세요.
import streamlit as st
import pandas as pd
import numpy as np

# 제목
st.title("내 수업 시간표")

# 정적 시간표 (st.table)
st.markdown("### 전체 수업")
# 시간표 데이터프레임 생성 (사용자 데이터 활용)
data = {
    '요일' : ['월', '월', '월', '월', '수', '수', '수', '금', '금', '금'],
    '시간' : ['11:00~12:15', '12:30~13:45', '15:00~15:50', '16:00~17:50', '11:00~12:15', '12:30~13:45', '15:00~15:50', '10:00~12:50', '13:00~14:50', '15:00~16:50'],
    '과목명' : ['대학 글쓰기1', '동아시아의 역사 분쟁', '수학 2', '산림과학개론', '대학 글쓰기1', '동아시아의 역사 분쟁', '수학 2', '컴탐실', '화학 실험', '수학 연습 2']
}
df = pd.DataFrame(data)
st.table(df)

# 3. 수업 정보 (st.json)
st.markdown("### 수업 정보")
# 여러 과목에 대한 상세 정보를 포함하도록 JSON 데이터 구조를 변경 (견본 참고)
json_data = {
    "대학 글쓰기1": {
        "교수": "김효재",
        "학점": 2,
        "강의실": "83동 203호"
    },
    "동아시아의 역사 분쟁": {
        "교수": "김유정",
        "학점": 3,
        "강의실": "7동 106호"
    },
    "수학 2": {
        "교수": "남계숙",
        "학점": 2,
        "강의실": "25동 104호"
    },
    "산림과학개론": {
        "교수": "산림과학부",
        "학점": 2,
        "강의실": "75-1동 203호"
    },
    "컴탐실": {
        "교수": "변해선",
        "학점": 3,
        "강의실": "26동 104호"
    },
    "화학 실험": {
        "교수": "이현우",
        "학점": 1,
        "강의실": "26동 506호"
    },
    "수학 연습 2": {
        "교수": "김대용",
        "학점": 1,
        "강의실": "24동 210호"
}}

st.json(json_data)


# 4. 이번 학기 요약 (st.metric)
st.markdown("### 이번 학기 요약")

# st.columns를 사용하여 두 개의 메트릭을 좌우로 나란히 배치합니다.
col1, col2 = st.columns(2)

# 총 수업 수 (중복 과목을 제외한 고유 과목 수)
num_unique_courses = len(df['과목명'].unique())

# 첫 번째 컬럼(col1)에 수강 과목 수 metric을 배치합니다.
with col1:
    st.metric(label="수강 과목 수", value=num_unique_courses, delta=num_unique_courses - 4, delta_color="normal")

# 총 학점 계산 로직: json_data에서 모든 학점을 합산합니다.
total_credits = sum(item['학점'] for item in json_data.values())

# 두 번째 컬럼(col2)에 총 학점 metric을 배치합니다.
with col2:
    st.metric(label="총 학점", value=total_credits, delta=total_credits - 12, delta_color="normal")