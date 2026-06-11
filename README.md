# AIDEOM-VN — Web báo cáo

Website trình bày báo cáo AIDEOM-VN từ file HTML.

## Cách 1 — GitHub Pages (đơn giản nhất, cho HTML tĩnh)
1. Tạo repository mới trên GitHub (ví dụ `aideom-vn`).
2. Upload file `index.html` (và các ảnh nếu có) vào repo.
3. Vào **Settings → Pages → Source = main branch → /root → Save**.
4. Sau ~1 phút, web chạy tại: `https://<tên-github>.github.io/aideom-vn/`

## Cách 2 — Streamlit Community Cloud (miễn phí)
1. Đẩy 3 file `index.html`, `streamlit_app.py`, `requirements.txt` lên repo GitHub.
2. Vào https://share.streamlit.io → **New app** → chọn repo → main file = `streamlit_app.py`.
3. Bấm **Deploy**. Web chạy tại `https://<app>.streamlit.app`

## Chạy thử cục bộ
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
