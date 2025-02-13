import streamlit as st
import random
import string
import time

# 1. 상품 목록
products = [
    {"name": "스마트폰", "price": 500000},
    {"name": "노트북", "price": 1000000},
    {"name": "스마트워치", "price": 200000},
    {"name": "이어폰", "price": 150000},
    {"name": "디지털 카메라", "price": 400000}
]

# 2. 배송 번호 생성 함수
def generate_delivery_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# 3. Streamlit UI 설정
st.set_page_config(page_title="배송 조회 서비스", page_icon="📦", layout="centered")

# 세션 상태 초기화
if 'orders' not in st.session_state:
    st.session_state.orders = {}

if 'current_order_id' not in st.session_state:
    st.session_state.current_order_id = ""

# 탭 메뉴
tab = st.radio("탭을 선택하세요", ("상품 주문", "배송 상태 확인"))

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

            st.write(f"🆕 주문이 완료되었습니다! **배송 번호:** `{delivery_number}`")
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
            st.write(f"📦 **배송 번호:** `{order_id_input}`")
            st.write(f"📌 **주문 상품:** {order['product']}")
            st.write(f"🚀 **배송 상태:** `{order['status']}`")

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