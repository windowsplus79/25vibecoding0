import streamlit as st

# ✅ 페이지 설정은 반드시 최상단에
st.set_page_config(page_title="MBTI 진로 추천기", page_icon="❄️", layout="centered")

# 눈 효과 (기본 내장)
st.snow()

# 타이틀
st.title("🔮 MBTI로 보는 진로 추천")
st.markdown("당신의 **MBTI**를 선택하면 어울리는 직업을 추천해드려요! 💼✨")

# MBTI 목록 및 추천 직업 딕셔너리
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_jobs = {
    "INTJ": ("전략 컨설턴트 💼", "시스템 설계자 🛠️", "데이터 과학자 📊"),
    "INTP": ("연구원 🔬", "이론 물리학자 🧪", "UX 디자이너 🎨"),
    "ENTJ": ("CEO 👩‍💼", "변호사 ⚖️", "프로젝트 매니저 📋"),
    "ENTP": ("기업가 🚀", "마케팅 디렉터 📣", "발명가 💡"),
    "INFJ": ("상담가 🧘", "심리학자 🧠", "작가 ✍️"),
    "INFP": ("예술가 🎨", "작가 📚", "사회운동가 ✊"),
    "ENFJ": ("교사 🧑‍🏫", "HR 매니저 🧑‍💼", "사회복지사 🤝"),
    "ENFP": ("크리에이터 🎥", "기획자 📅", "홍보 전문가 📢"),
    "ISTJ": ("회계사 📊", "공무원 🏛️", "엔지니어 🏗️"),
    "ISFJ": ("간호사 👩‍⚕️", "초등교사 🏫", "행정직원 🗂️"),
    "ESTJ": ("관리자 📋", "군인 🪖", "정치인 🏛️"),
    "ESFJ": ("간호 관리자 🏥", "영업 매니저 📞", "교직원 🧑‍🏫"),
    "ISTP": ("기술자 🔧", "파일럿 ✈️", "탐험가 🧭"),
    "ISFP": ("플로리스트 🌸", "사진작가 📸", "패션 디자이너 👗"),
    "ESTP": ("세일즈맨 🗣️", "운동선수 🏋️", "이벤트 플래너 🎉"),
    "ESFP": ("배우 🎭", "가수 🎤", "방송인 📺")
}

# 선택 박스
selected_mbti = st.selectbox("🎯 당신의 MBTI를 선택하세요", mbti_types)

# 결과 표시
if selected_mbti:
    st.subheader(f"💡 {selected_mbti}에게 어울리는 직업")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.success("이 직업들이 당신의 성향과 잘 어울릴 수 있어요! ✨")
