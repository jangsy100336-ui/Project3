st.markdown("""
<style>
.stApp {
    background-color: #0b1b3a;
    color: white;
}

/* 디스플레이 */
.display {
    background-color: #001f5c;
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: right;
    font-size: 42px;   /* 🔥 기존보다 조금 증가 */
    font-weight: bold;
    margin-bottom: 20px;
}

/* 🔥 모든 버튼 동일 크기 + 글자만 크게 */
div.stButton > button {
    background-color: #001f5c;
    color: white;
    border-radius: 16px;
    height: 85px;
    font-size: 30px;   /* 🔥 핵심: 문자 크기 증가 */
    font-weight: bold;
    width: 100%;
    transition: 0.1s;
}

/* 눌림 효과 */
div.stButton > button:active {
    transform: scale(0.95);
    background-color: #003080;
}

div.stButton > button:hover {
    background-color: #003080;
}
</style>
""", unsafe_allow_html=True)
