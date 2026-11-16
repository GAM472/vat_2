import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp, h1, h2, h3, p, div, span, input {
    font-family: 'IBM Plex Sans Thai', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=1000.0)
discount_percent = st.number_input("กรอกส่วนลด (%):", min_value=0.0, max_value=100.0, value=20.0)

discount = price * (discount_percent / 100)
price_after_discount = price - discount
vat = price_after_discount * 0.07
net_price = price_after_discount + vat

st.divider()

st.write(f"• ส่วนลด ({discount_percent:.0f}%): -{discount:.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {price_after_discount:.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat:.2f} บาท")

st.header(f"• ราคาสุทธิที่ต้องจ่าย: {net_price:.2f} บาท")

st.divider()

st.write("นางสาวธัญพิมล แสนใจพรม เลขที่ 14 ม.4/5")
