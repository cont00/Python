import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import random
import string
import time
import json
import os

# 1. Streamlit UI 설정
st.set_page_config(page_title="배송 조회 서비스", page_icon="📦", layout="centered")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 음성을 입력하세요...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language='ko-KR')
            return text
        except sr.UnknownValueError:
            return "음성을 인식할 수 없습니다. 다시 시도해주세요."
        except sr.RequestError:
            return "음성 인식 서비스를 사용할 수 없습니다."

# 2. 상품 목록
products = [
    {"name": "스마트폰", "price": 500000},
    {"name": "노트북", "price": 1000000},
    {"name": "스마트워치", "price": 200000},
    {"name": "이어폰", "price": 150000},
    {"name": "디지털 카메라", "price": 400000}
]

# 3. 배송 번호 생성 함수
def generate_delivery_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))



# 세션 상태 초기화
if 'orders' not in st.session_state:
    st.session_state.orders = {}

if 'current_order_id' not in st.session_state:
    st.session_state.current_order_id = ""

# 탭 메뉴
tab = st.radio("탭을 선택하세요", ("상품 주문", "배송 상태 확인", "Chatbot 상담"))

# 4. 상품 주문 탭
if tab == "상품 주문":
    st.subheader("🛒 상품 주문")

    # 상품 목록 표시
    product_names = [product["name"] for product in products]
    selected_product = st.selectbox("📌 구매할 상품 선택", product_names)

    # 선택된 상품 정보 표시
    if selected_product:
        selected_product_info = next(product for product in products if product["name"] == selected_product)
        st.write(f"**상품명:** {selected_product_info['name']}")
        st.write(f"**가격:** {selected_product_info['price']} 원")

    # 주문하기 버튼
    if st.button("✅ 주문하기"):
        if selected_product:
            # 배송 번호 생성
            delivery_number = generate_delivery_number()
            
            # 주문 상태 초기값 설정
            delivery_status = "주문 접수 완료"
            order_time = time.time()
            
            # 주문 정보 저장
            st.session_state.orders[delivery_number] = {
                "product": selected_product_info['name'],
                "status": delivery_status,
                "order_time": order_time,
                "refund_requested": False
            }
            
            # 현재 주문한 배송 번호 저장
            st.session_state.current_order_id = delivery_number

            st.write(f"🆕 주문이 완료되었습니다! **배송 번호:** {delivery_number}")
        else:
            st.write("상품을 선택해 주세요.")

# 5. 배송 상태 확인 탭
if tab == "배송 상태 확인":
    st.subheader("🚚 배송 상태 확인")

    # 배송 번호 입력 필드 (입력값 유지)
    order_id_input = st.text_input("📦 배송 번호를 입력하세요:", st.session_state.current_order_id)

    # 조회 버튼
    if st.button("🔍 배송 상태 확인"):
        if order_id_input:
            if order_id_input in st.session_state.orders:
                st.session_state.current_order_id = order_id_input  # 입력된 배송번호 저장
                order = st.session_state.orders[order_id_input]
                
                # 🚀 배송 상태 자동 갱신 (시간 경과에 따라 변경)
                elapsed_time = time.time() - order["order_time"]
                if elapsed_time > 60 and order["status"] == "주문 접수 완료":
                    st.session_state.orders[order_id_input]["status"] = "배송 중"
                elif elapsed_time > 180 and order["status"] == "배송 중":
                    st.session_state.orders[order_id_input]["status"] = "배송 완료"

                st.rerun()  # 🚀 즉시 반영

            else:
                st.write("🚫 해당 배송 번호는 존재하지 않습니다. 다시 확인해주세요.")
        else:
            st.write("⚠ 배송 번호를 입력하세요.")

    # ✅ 주문 정보 유지하면서 표시
    if st.session_state.current_order_id:
        order_id_input = st.session_state.current_order_id
        order = st.session_state.orders.get(order_id_input, None)

        if order:
            st.write(f"📦 **배송 번호:** {order_id_input}")
            st.write(f"📌 **주문 상품:** {order['product']}")
            st.write(f"🚀 **배송 상태:** {order['status']}")

            # ✅ 환불 버튼 (주문 접수 상태에서만 가능)
            if order["status"] == "주문 접수 완료":
                if st.button("❌ 환불 요청"):
                    # ✅ 🚀 상태를 변경하고 즉시 반영
                    st.session_state.orders[order_id_input]["status"] = "주문 접수 취소"
                    st.session_state.orders[order_id_input]["refund_requested"] = True
                    st.rerun()  # 🚀 즉시 반영

            # 이미 환불된 경우 메시지 출력
            elif order["status"] == "주문 접수 취소":
                st.write("✅ 주문이 환불되었습니다.")

# 6. Chatbot 상담 탭
if tab == "Chatbot 상담":
    st.markdown("<h2 style='text-align: center;'>💬 물품 상담 Chatbot</h2>", unsafe_allow_html=True)

    # Gemini API 키 설정
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # 상담 내역 저장 파일
    CHAT_HISTORY_FILE = "chat_history.json"

    # 상담 내역 불러오기 및 저장
    CHAT_HISTORY_FILE = "chat_history.json"
    def load_chat_history():
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_chat_history(conversation):
        with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(conversation, file, ensure_ascii=False, indent=4)

    if 'conversation' not in st.session_state:
        st.session_state.conversation = load_chat_history()

    # 입력 방식 선택
    input_method = st.radio("입력 방식을 선택하세요:", ("텍스트 입력", "음성 인식"))

    if input_method == "텍스트 입력":
        user_input = st.text_input("질문을 입력하세요:", key="chat_input")
        submit = st.button("💬 상담 진행")
    elif input_method == "음성 인식":
        if st.button("🎤 음성 인식 시작"):
            user_input = recognize_speech()
            st.text(f"🎙️ 인식된 내용: {user_input}")
            submit = True
        else:
            user_input = ""
            submit = False

    if submit and user_input.strip():
        st.session_state.conversation.append(f"사용자: {user_input}")
        
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        chatbot_reply = response.text if response else "죄송합니다. 답변을 생성할 수 없습니다."

        st.session_state.conversation.append(f"Chatbot: {chatbot_reply}")
        save_chat_history(st.session_state.conversation)
        st.rerun()

    # ✅ 제품 목록 정의
    product_list = [
        {"name": "스마트폰", "price": 500000, "desc": "고성능 카메라와 빠른 성능을 자랑하는 스마트폰"},
        {"name": "노트북", "price": 1000000, "desc": "휴대성과 성능을 겸비한 최신 노트북"},
        {"name": "스마트워치", "price": 200000, "desc": "건강 관리 기능이 포함된 스마트워치"},
        {"name": "이어폰", "price": 150000, "desc": "노이즈 캔슬링이 지원되는 무선 이어폰"},
        {"name": "디지털 카메라", "price": 400000, "desc": "고화질 촬영이 가능한 디지털 카메라"}
    ]

    # 🚀 주문 및 추천 정보를 가져오기
    def get_order_summary():
        order_summary = []
        for order_id, details in st.session_state.orders.items():
            status = details["status"]
            if status == "주문 접수 완료":
                order_summary.append(f"- 주문 상품: {details['product']} (배송 번호: {order_id})")
            elif status == "주문 접수 취소":
                order_summary.append(f"- 환불된 상품: {details['product']} (배송 번호: {order_id})")
        return "\n".join(order_summary) if order_summary else "현재 주문 내역이 없습니다."

    def get_product_info():
        return "\n".join([f"- {p['name']}: {p['desc']} (가격: {p['price']}원)" for p in product_list])

    # 세션 상태 초기화
    if 'conversation' not in st.session_state:
        st.session_state.conversation = load_chat_history()

    # ✅ 최근 상담 내역만 유지 (최대 5개)
    MAX_HISTORY = 5
    conversation = st.session_state.conversation[-MAX_HISTORY:]

    # ✅ "상담 내역 전체 보기" 버튼 추가
    show_full_history = st.checkbox("📜 상담 내역 전체 보기", False)
    if show_full_history:
        conversation = st.session_state.conversation  # 전체 내역 보기

    # 🚀 세련된 UI 스타일 적용
    chat_container = """
    <style>
    /* 기본적인 채팅 화면 스타일 */
    .chat-container {
        max-width: 700px;
        margin: 20px auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-family: 'Roboto', sans-serif;
    }

    /* 사용자 메시지 스타일 (오른쪽 정렬) */
    .chat-bubble-user {
        background-color: #DCF8C6;
        padding: 12px 18px;
        border-radius: 18px;
        margin: 8px 0;
        text-align: right;
        max-width: 80%;
        word-wrap: break-word;
        display: inline-block;
        float: right;  /* 오른쪽 정렬 */
    }

    /* 챗봇 메시지 스타일 (왼쪽 정렬) */
    .chat-bubble-bot {
        background-color: #EAEAEA;
        padding: 12px 18px;
        border-radius: 18px;
        margin: 8px 0;
        text-align: left;
        max-width: 80%;
        word-wrap: break-word;
        display: inline-block;
        float: left;  /* 왼쪽 정렬 */
    }

    /* 채팅 입력 창 스타일 */
    .chat-input-container {
        display: flex;
        gap: 15px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .chat-input {
        flex: 1;
        padding: 14px;
        font-size: 16px;
        border-radius: 8px;
        border: 1px solid #ddd;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .chat-button {
        padding: 12px 24px;
        font-size: 16px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .chat-button:hover {
        background-color: #0056b3;
    }

    .chat-button:active {
        background-color: #003d7a;
    }

    /* 상담 내역 초기화 버튼 스타일 */
    .clear-history-button {
        background-color: #FF5722;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
        margin-top: 20px;
        display: block;
        width: 100%;
    }

    .clear-history-button:hover {
        background-color: #e64a19;
    }

    /* 상담 내역 전체 보기 체크박스 스타일 */
    .checkbox-label {
        font-size: 14px;
        color: #555;
    }
    </style>
    """
    st.markdown(chat_container, unsafe_allow_html=True)

    # 상담 내역 표시
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for message in conversation:
        if message.startswith("사용자:"):
            st.markdown(f"<div class='chat-bubble-user'>{message[4:]}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-bot'>{message[8:]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 질문 입력 UI 개선 (더 넓고, 보기 좋게)
    col1, col2 = st.columns([4, 1])
    with col1:
        # 텍스트 입력창을 상태로 관리하여 초기화 가능하도록 설정
        user_input = st.text_input("질문을 입력하세요:", key="chat_input", placeholder="예) 스마트폰 추천해줘", help="상품 추천, 배송 상태, 환불 관련 질문 가능")

    with col2:
        # 버튼 클릭을 확인하고, 입력이 있을 때만 실행되도록 변경
        if st.button("💬 상담 진행", help="챗봇과 상담을 시작합니다."):
            if user_input.strip():  # 빈 입력을 방지
                # 기존 대화에 질문 추가
                st.session_state.conversation.append(f"사용자: {user_input}")

                # 🚀 Gemini API 호출 시 주문 + 제품 정보 포함
                model = genai.GenerativeModel("gemini-pro")
                prompt = f"""
                사용자와의 대화에서 아래 정보를 참고하여 답변하세요.
                --- 
                [현재 주문 정보]  
                {get_order_summary()}  
                [제품 정보]  
                {get_product_info()}  
                ---
                사용자 질문: {user_input}
                """
                response = model.generate_content(prompt)
                chatbot_reply = response.text if response else "죄송합니다. 답변을 생성할 수 없습니다."

                # 답변을 대화에 추가
                st.session_state.conversation.append(f"Chatbot: {chatbot_reply}")

                # 상담 내역 저장
                save_chat_history(st.session_state.conversation)
                
                # 질문 입력 텍스트를 비우기 위해 'chat_input' 위젯을 새로 고침
                st.rerun()  # 화면을 새로 고침하여 입력 필드 초기화

        # 상담 내역 초기화 버튼
        if st.button("🗑️ 상담 내역 초기화", help="이전 상담 기록을 삭제합니다."):
            # 상담 내역을 비우고 저장
            st.session_state.conversation = []
            save_chat_history([])  # 빈 대화 내역을 저장
            st.write("✅ 상담 내역이 초기화되었습니다.")
            st.rerun()  # 화면을 새로 고침하여 초기화 반영