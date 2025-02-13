import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# 필요한 패키지 확인 및 다운로드
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# 감정 분석기 초기화
sia = SentimentIntensityAnalyzer()

# Streamlit UI 구성
st.title("AI 기반 감정 분석 플랫폼")
st.write("텍스트를 입력하면 감정을 분석해드립니다.")

# 사용자 입력
user_input = st.text_area("분석할 텍스트를 입력하세요:")

if st.button("감정 분석 실행"):
    if user_input:
        sentiment_score = sia.polarity_scores(user_input)
        
        # 감정 분석 결과 분류
        if sentiment_score['compound'] >= 0.05:
            sentiment = "긍정 😊"
        elif sentiment_score['compound'] <= -0.05:
            sentiment = "부정 😡"
        else:
            sentiment = "중립 😐"
        
        # 결과 출력
        st.subheader("분석 결과")
        st.write(f"감정 분석 결과: **{sentiment}**")
        st.write(f"세부 점수: {sentiment_score}")
    else:
        st.warning("텍스트를 입력해주세요!")