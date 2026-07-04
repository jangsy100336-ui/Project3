import streamlit as st

# -------------------------
# 페이지 설정
# -------------------------
st.set_page_config(page_title="iOS 계산기", layout="centered")

# -------------------------
# 스타일
# -------------------------
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
    padding: 28px;
    border-radius: 15px;
    text-align: right;
    font-size: 48px;   /* 🔥 살짝 증가 */
    font-weight: bold;
    margin-bottom: 10px;
}

/* 히스토리 */
.history {
    text-align: right;
    font-size: 18px;
    opacity: 0.7;
    margin-bottom: 10px;
}

/* 🔥 모든 버튼 동일 + 글자 더 크게 */
div.stButton > button {
    background-color: #001f5c;
    color: white;
    border-radius: 18px;
    height: 85px;
    font-size: 34px;   /* 🔥 핵심 증가 */
    font-weight: bold;
    width: 100%;
    transition: 0.1s;
}

/* 눌림 효과 */
div.stButton > button:active {
    transform: scale(0.94);
    background-color: #003080;
}

div.stButton > button:hover {
    background-color: #003080;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 상태
# -------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = ""

# -------------------------
# 계산
# -------------------------
def safe_eval(expr):
    try:
        expr = expr.replace("×", "*").replace("÷", "/")
        return str(eval(expr))
    except:
        return "Error"

# -------------------------
# 입력 처리
# -------------------------
def press(key):
    if key == "AC":
        st.session_state.expr = ""
        st.session_state.history = ""

    elif key == "⌫":
        st.session_state.expr = st.session_state.expr[:-1]

    elif key == "=":
        st.session_state.history = st.session_state.expr
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
# 화면
# -------------------------
st.markdown("<h1 style='text-align:center;'>🧮 iOS 계산기</h1>", unsafe_allow_html=True)

# 히스토리
st.markdown(f"<div class='history'>{st.session_state.history}</div>", unsafe_allow_html=True)

# 디스플레이
st.markdown(f"<div class='display'>{st.session_state.expr or '0'}</div>", unsafe_allow_html=True)

# -------------------------
# 버튼
# -------------------------
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
row5 = st.columns(4)

# Row 1
with row1[0]: st.button("AC", use_container_width=True, on_click=press, args=("AC",))
with row1[1]: st.button("⌫", use_container_width=True, on_click=press, args=("⌫",))
with row1[2]: st.button("%", use_container_width=True, on_click=press, args=("%",))
with row1[3]: st.button("÷", use_container_width=True, on_click=press, args=("÷",))

# Row 2
with row2[0]: st.button("7", use_container_width=True, on_click=press, args=("7",))
with row2[1]: st.button("8", use_container_width=True, on_click=press, args=("8",))
with row2[2]: st.button("9", use_container_width=True, on_click=press, args=("9",))
with row2[3]: st.button("×", use_container_width=True, on_click=press, args=("×",))

# Row 3
with row3[0]: st.button("4", use_container_width=True, on_click=press, args=("4",))
with row3[1]: st.button("5", use_container_width=True, on_click=press, args=("5",))
with row3[2]: st.button("6", use_container_width=True, on_click=press, args=("6",))
with row3[3]: st.button("-", use_container_width=True, on_click=press, args=("-"))

# Row 4
with row4[0]: st.button("1", use_container_width=True, on_click=press, args=("1",))
with row4[1]: st.button("2", use_container_width=True, on_click=press, args=("2",))
with row4[2]: st.button("3", use_container_width=True, on_click=press, args=("3",))
with row4[3]: st.button("+", use_container_width=True, on_click=press, args=("+",))

# Row 5
with row5[0]: st.button("±", use_container_width=True, on_click=press, args=("±",))
with row5[1]: st.button("0", use_container_width=True, on_click=press, args=("0",))
with row5[2]: st.button(".", use_container_width=True, on_click=press, args=(".",))
with row5[3]: st.button("=", use_container_width=True, on_click=press, args=("=",))
