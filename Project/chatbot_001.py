import streamlit as st
import pyttsx3
import speech_recognition as sr

# 챗봇 응답 생성 함수
def generate_bot_response(user_input):
    lower_input = user_input.lower()
    
    responses = {
        "안녕하세요": "안녕하세요! 쇼핑몰에 오신 것을 환영합니다. 무엇을 도와드릴까요?",
        "주문": "주문을 원하시는군요! 어떤 상품을 주문하시겠어요?",
        "상품": "저희 쇼핑몰에서는 다양한 상품을 판매하고 있습니다. 카테고리별로 소개해 드릴까요?",
        "의류": "의류 카테고리: 티셔츠(15,000원), 청바지(30,000원), 후드티(25,000원). 원하는 상품을 선택해 주세요!",
        "전자제품": "전자제품 카테고리: 스마트폰(500,000원), 노트북(1,200,000원), 이어폰(50,000원). 원하는 상품을 선택해 주세요!",
        "감사합니다": "감사합니다! 좋은 하루 되세요."
    }

    # 사전에서 키워드 매칭
    for key, response in responses.items():
        if key in lower_input:
            return response

    return "죄송합니다. 이해하지 못했어요. 다시 말씀해 주세요."

# TTS (Text-to-Speech) 기능
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# STT (Speech-to-Text) 기능
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("음성을 입력하세요...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="ko-KR")
            return text
        except sr.UnknownValueError:
            return "음성을 인식할 수 없습니다."
        except sr.RequestError:
            return "음성 인식 서비스에 문제가 발생했습니다."

# Streamlit UI
st.title("고객 상담 챗봇")

# 대화 내역 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [("챗봇", "안녕하세요! 무엇을 도와드릴까요?")]

# 대화 내역 표시
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")

# 사용자 입력 (텍스트)
user_input = st.text_input("여기에 입력하세요:", key="user_input")

# 음성 입력 버튼
if st.button("음성 입력"):
    speech_text = recognize_speech()
    if speech_text:
        st.session_state.chat_history.append(("고객", speech_text))
        bot_response = generate_bot_response(speech_text)
        st.session_state.chat_history.append(("챗봇", bot_response))
        speak(bot_response)
        st.rerun()

# 메시지 전송 버튼
if st.button("보내기"):
    if user_input.strip():
        st.session_state.chat_history.append(("고객", user_input))
        bot_response = generate_bot_response(user_input)
        st.session_state.chat_history.append(("챗봇", bot_response))
        speak(bot_response)
        st.rerun()

# 대화 초기화 버튼
if st.button("대화 초기화"):
    st.session_state.chat_history = [("챗봇", "안녕하세요! 무엇을 도와드릴까요?")]
    st.rerun()