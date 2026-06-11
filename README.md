# AIDEOM-VN — Website báo cáo phân tích

> **AI-driven Economic Decision-Making for Vietnam**
> Mười hai mô hình định lượng trả lời một câu hỏi: Việt Nam nên phân bổ nguồn lực thế nào trong kỉ nguyên trí tuệ nhân tạo?

---

#

## 🗂️ Nội dung trang web

**Tổng quan** — Dẫn nhập + bốn chỉ số chủ chốt + biểu đồ bong bóng 10 ngành.

**Cấp độ 1 · Nền tảng (Bài 01–03)** — Động lực tăng trưởng đến từ đâu: hàm sản xuất Cobb-Douglas mở rộng, quy hoạch tuyến tính, chỉ số ưu tiên ngành.

**Cấp độ 2 · Phân bổ (Bài 04–06)** — Chia nguồn lực hiệu quả và công bằng: LP phân bổ vùng, MIP chọn dự án, TOPSIS đa tiêu chí.

**Cấp độ 3 · Đánh đổi (Bài 07–09)** — Khi không thể tối ưu mọi thứ: mặt Pareto NSGA-II, tối ưu động, dịch chuyển lao động.

**Cấp độ 4 · Bất định & tích hợp (Bài 10–12)** — Quy hoạch ngẫu nhiên, học tăng cường Q-learning, mô hình tích hợp AIDEOM-VN.

**Bản đồ 10 ngành** — Bảng chiến lược ghép ưu tiên × sẵn sàng AI × việc làm ròng.

**Kết luận** — Bốn luận điểm xuyên suốt + đánh giá độ tin cậy.

---

##  Bốn con số đáng nhớ

- **+25,8%** — TFP tăng 2020–2025 (gần một nửa tăng trưởng đến từ hiệu quả)
- **14.472** — GDP dự báo 2030 (nghìn tỷ)
- **14,0 triệu** — việc làm ròng do AI (80,7% dồn vào CNTT)
- **23,7%** — cái giá GDP phải trả cho công bằng vùng miền

> **Thông điệp xuyên suốt:** “AI không có nhân lực là vốn chết” — ba phương pháp độc lập cùng cho một kết luận: đầu tư AI đơn độc luôn thua chiến lược cân bằng.

---

##  Cách chạy

### Xem trực tiếp
File `index.html` là trang web hoàn chỉnh, **tự chứa** (biểu đồ nhúng dạng base64) — chỉ cần mở bằng trình duyệt là chạy, không cần thư mục ảnh kèm theo.

### Đưa lên GitHub Pages
1. Tạo repository **Public** trên GitHub.
2. Upload `index.html` vào thư mục gốc.
3. **Settings → Pages → Source = Deploy from a branch → main / (root) → Save**.
4. Chờ 1–2 phút, web chạy tại `https://<tên-github>.github.io/<tên-repo>/`

### Chạy bằng Streamlit
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

##  Cấu trúc thư mục

```
.
├── index.html          # Trang web báo cáo (tự chứa, ~1,3 MB)
├── streamlit_app.py    # App Streamlit bọc file HTML
├── requirements.txt    # Thư viện cần cài
└── README.md           # File này
```

---

*Số liệu tính trực tiếp từ mã nguồn Google Colab của 12 bài tập.*
