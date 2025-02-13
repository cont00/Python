import streamlit as st
import openai
import os

# OpenAI API Key를 환경변수에서 불러오기
openai.api_key = os.getenv("GOOGLE_API_KEY")

def get_chatbot_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 최신 모델
        messages=[
            {"role": "user", "content": user_message}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

# 페이지 레이아웃 설정
st.set_page_config(page_title="고객 상담 챗봇", page_icon="🤖", layout="centered")

# 헤더
st.title("고객 상담 챗봇")
st.write("챗봇과 대화해보세요!")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 대화 출력
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"<div style='background-color:#DCF8C6;padding:10px;margin:10px;border-radius:10px;'><strong>고객:</strong> {message['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#E4E6E7;padding:10px;margin:10px;border-radius:10px;'><strong>챗봇:</strong> {message['text']}</div>", unsafe_allow_html=True)

# 입력창 고정
user_input = st.text_input("메시지를 입력하세요...", key="user_input", max_chars=200)

# 메시지 전송
if user_input:
    st.session_state["messages"].append({"role": "user", "text": user_input})
    bot_response = get_chatbot_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "text": bot_response})
    st.experimental_rerun()  # 페이지 새로고침하여 대화 갱신

# 페이지에 대한 스타일 설정 (CSS로 UI 편집)
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)