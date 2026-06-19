import streamlit as st
import logging
logging.getLogger("streamlit.runtime.scriptrunner_utils.script_run_context").setLevel(logging.ERROR)
# 페이지 설정
st.set_page_config(page_title="반도체학과 1학년 1학기 학점 계산기", page_icon="🎓")

st.title("🎓 반도체공학과 1학년 1학기 학점 계산기(공식 홈페이지 아닙니다.)")
st.write("각 과목의 성적을 선택하면 자동으로 평점이 계산됩니다.")

# 과목 데이터 정의
subjects_3 = {"반도체 산업의 이해": 3, "파이썬 및 인공지능": 3, "수학의 이해1": 3}
subjects_2 = {"글쓰기와 커뮤니케이션": 2, "벤처와 산업가 이해": 2, "영어와 비판적 사고": 2, "일반물리학1": 2}
subjects_1 = {"일반물리실험": 1}

grade_points = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

# 성적 선택 함수
def create_grade_selector(subjects):
    scores = {}
    for sub, credit in subjects.items():
        scores[sub] = st.selectbox(f"{sub} ({credit}학점)", list(grade_points.keys()))
    return scores

# UI 구성
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("3학점 과목")
    scores_3 = create_grade_selector(subjects_3)
with col2:
    st.subheader("2학점 과목")
    scores_2 = create_grade_selector(subjects_2)
with col3:
    st.subheader("1학점 과목")
    scores_1 = create_grade_selector(subjects_1)

# 계산 로직
total_points = 0
total_credits = 0

all_scores = {**scores_3, **scores_2, **scores_1}
all_subjects = {**subjects_3, **subjects_2, **subjects_1}

for sub, grade in all_scores.items():
    credit = all_subjects[sub]
    total_points += grade_points[grade] * credit
    total_credits += credit

# 결과 출력
st.divider()
gpa = total_points / total_credits if total_credits > 0 else 0
st.metric(label="최종 예상 평점", value=f"{gpa:.2f} / 4.5")
st.write(f"총 이수 학점: {total_credits}학점")
