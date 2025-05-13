import streamlit as st
from streamlit_extras.snow import snow

# 눈 효과 실행
snow()

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", page_icon="✨", layout="centered")

# 스타일 적용
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #e0c3fc, #8ec5fc);
        padding: 2rem;
        border-radius: 10px;
        color: white;
    }
    h1, h2 {
        text-shadow: 0 0 10px #fff, 0 0 20px #ff00ff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🔮 MBTI로 보는 진로 추천</h1>", unsafe_allow_html=True)
st.markdown("당신의 **MBTI**를 선택하면 어울리는 직업을 추천해드려요! 💼✨")

# MBTI 로직 그대로 유지
mbti_types = [...]
mbti_jobs = {...}

selected_mbti = st.selectbox("✨ MBTI를 선택하세요", mbti_types)

if selected_mbti:
    st.markdown(f"### 💡 {selected_mbti}에게 어울리는 직업")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.success("이 직업들이 당신의 성향과 잘 어울릴 수 있어요! ✨")
