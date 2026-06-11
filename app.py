import streamlit as st

st.set_page_config(layout="wide", page_title="AIDEOM-VN")

# Thanh điều hướng Sidebar dùng chung
st.sidebar.markdown("""
### VN AIDEOM-VN
*Mô hình ra quyết định phát triển kinh tế VN trong kỷ nguyên AI*
---
📊 **Dữ liệu:** NSO, MoST, MIC, MPI, WB, GII 2025  
🛠️ **Stack:** Streamlit · Plotly · SciPy · PuLP  
📖 *Dựa trên giáo trình AIDEOM-VN 2026*
""", unsafe_allow_html=True)

st.title("Hệ thống Mô phỏng Kinh tế & Quyết định Chính sách AIDEOM-VN")
st.write("---")
st.markdown("""
### Hướng dẫn nhanh:
Hệ thống đã được dựng sẵn bộ khung **12 Bài tập mô phỏng**. 
Vui lòng nhìn sang **Thanh điều hướng bên trái** và click chọn từng bài để xem giao diện tính toán mẫu.
""")