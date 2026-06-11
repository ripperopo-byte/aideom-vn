# -*- coding: utf-8 -*-
"""
AIDEOM-VN | Web trình bày báo cáo từ file HTML
Chạy cục bộ:  streamlit run streamlit_app.py
"""
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="AIDEOM-VN | Báo cáo",
    page_icon="📊",
    layout="wide",
)

# --- Đọc file HTML cùng thư mục ---
HTML_FILE = Path(__file__).parent / "index.html"

st.title("📊 AIDEOM-VN — Mô hình ra quyết định phát triển kinh tế")
st.caption("Trần Đình Hướng — 23050491 — QH-2023-E KTPT 3")

if HTML_FILE.exists():
    html = HTML_FILE.read_text(encoding="utf-8")
    # height lớn + scrolling để cuộn mượt toàn trang
    components.html(html, height=2000, scrolling=True)
else:
    st.error("Không tìm thấy file index.html. Hãy đặt file HTML cùng thư mục và đổi tên thành index.html")
