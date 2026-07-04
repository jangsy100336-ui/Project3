import streamlit as st
import re

# -------------------------
# 페이지 설정
# -------------------------
st.set_page_config(page_title="계산기", layout="centered")

# -------------------------
# 스타일
# -------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1b3a;
    color: white;
}

h1, h2, h3, p, div {
    color: white !important;
}

/* 버튼 스타일 */
div.stButton > button {
    background-color: #001f5c;
    color: white;
    border-radius: 12px;
    height: 60px;
    font-size: 20px;
    font-weight: bold;
}

/* hover */
div.stButton > button:hover {
    background-color: #003080;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 상태 초기화
# -------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

# -------------------------
# 계산 함수
# -------------------------
def safe_eval(expr):
    try:
        expr = expr.replace("×", "*").replace("÷", "/")
        return str(eval(expr))
    except:
        return "Error"

# -------------------------
# 입력 처리 함수
# -------------------------
def press(key):
    if key == "AC":
        st.session_state.expr = ""

    elif key == "⌫":
        st.session_state.expr = st.session_state.expr[:-1]

    elif key == "=":
        st.session_state.expr = safe_eval(st.session_state.expr)

    elif key == "±":
        if st.session_state.expr:
            if st.session_state.expr.startswith("-"):
                st.session_state.expr = st.session_state.expr[1:]
            else:
                st.session_state.expr = "-" + st.session_state.expr

    elif key == "%":
        try:
            st.session_state.expr = str(float(st.session_state.expr) / 100)
        except:
            st.session_state.expr = "Error"

    else:
        st.session_state.expr += str(key)

# -------------------------
# 화면 출력
# -------------------------
st.markdown("<h1 style='text-align:center;'>🧮 계산기</h1>", unsafe_allow_html=True)

# 디스플레이
st.markdown(
    f"<h2 style='text-align:right; padding:10px; background:#001f5c; border-radius:10px;'>{st.session_state.expr or '0'}</h2>",
    unsafe_allow_html=True
)

st.write("---")

# -------------------------
# 버튼 배치 (모바일 계산기 구조)
# -------------------------
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
row5 = st.columns(4)

# Row 1
with row1[0]:
    if st.button("AC"): press("AC")
with row1[1]:
    if st.button("⌫"): press("⌫")
with row1[2]:
    if st.button("%"): press("%")
with row1[3]:
    if st.button("÷"): press("÷")

# Row 2
with row2[0]:
    if st.button("7"): press("7")
with row2[1]:
    if st.button("8"): press("8")
with row2[2]:
    if st.button("9"): press("9")
with row2[3]:
    if st.button("×"): press("×")

# Row 3
with row3[0]:
    if st.button("4"): press("4")
with row3[1]:
    if st.button("5"): press("5")
with row3[2]:
    if st.button("6"): press("6")
with row3[3]:
    if st.button("-"): press("-")

# Row 4
with row4[0]:
    if st.button("1"): press("1")
with row4[1]:
    if st.button("2"): press("2")
with row4[2]:
    if st.button("3"): press("3")
with row4[3]:
    if st.button("+"): press("+")

# Row 5
with row5[0]:
    if st.button("±"): press("±")
with row5[1]:
    if st.button("0"): press("0")
with row5[2]:
    if st.button("."): press(".")
with row5[3]:
    if st.button("="): press("=")
