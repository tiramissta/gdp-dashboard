import streamlit as st
import openai

# Lấy API key từ secrets (bảo mật)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI tạo nội dung cho Xưởng Bình Gốm")

product = st.text_input("Tên sản phẩm")
desc = st.text_area("Mô tả sản phẩm")
price = st.number_input("Giá (VNĐ)", min_value=0, step=1000)
tone = st.selectbox("Phong cách caption", ["Gần gũi", "Cảm hứng", "Trang trọng", "Hài hước"], index=0)

if st.button("Tạo caption AI"):
    if product and desc:
        prompt = (
            f"Viết caption Facebook quảng bá sản phẩm gốm '{product}' (giá {price} VNĐ). "
            f"Mô tả: {desc}. "
            f"Phong cách: {tone}. Dưới 100 từ, dễ hiểu, hấp dẫn khách hàng."
        )
        with st.spinner("AI đang suy nghĩ..."):
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=120,
                    temperature=0.8
                )
                st.success(response.choices[0].text.strip())
            except Exception as e:
                st.error(f"Lỗi khi gọi AI: {e}")
    else:
        st.warning("Nhập đủ tên và mô tả sản phẩm!")
