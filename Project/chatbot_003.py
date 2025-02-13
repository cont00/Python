import streamlit as st
import requests
import openai

# 제목
st.title("배송 상태 확인 챗봇")

# 사용자 입력 받기
order_id = st.text_input("주문 번호를 입력하세요:")

# 배송 상태 확인 함수
def get_delivery_status(order_id):
    # 예시 API URL (실제 URL과 연동해야 함)
    api_url = f"https://api.deliveryservice.com/status/{order_id}"

    # API 호출 (GET 방식)
    response = requests.get(api_url)
    
    # 응답이 성공적이면 상태 반환
    if response.status_code == 200:
        data = response.json()  # JSON 응답 파싱
        return data['status']  # 'status' 필드에 배송 상태 정보 있다고 가정
    else:
        return "배송 상태를 확인할 수 없습니다. 다시 시도해 주세요."
    

# 배송 상태 확인 버튼
if st.button("배송 상태 확인"):
    if order_id:
        # 여기서 배송 상태 확인 로직을 추가합니다.
        delivery_status = get_delivery_status(order_id)
        st.write(f"주문 번호 {order_id}의 배송 상태는: {delivery_status}")
    else:
        st.write("주문 번호를 입력해 주세요.")

# Gemini API를 통해 자연어 처리
def get_nlp_response(user_input):
    openai.api_key = "your-api-key-here"
    response = openai.Completion.create(
        model="gpt-4",  # 또는 사용할 모델에 맞게 설정
        prompt=user_input,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()