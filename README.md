# Thai Food Recipe Chatbot

ระบบแชทบอทสำหรับค้นหาและถามเกี่ยวกับสูตรอาหารไทย (Thai Food Recipe Chatbot)

## คุณสมบัติ (Features)

- ค้นหาสูตรอาหารไทยจากคำถามหรือชื่ออาหาร
- แสดงรายการวัตถุดิบและวิธีทำอย่างละเอียด
- รองรับทั้งภาษาไทยและภาษาอังกฤษ
- อินเตอร์เฟซที่ใช้งานง่ายด้วย Streamlit

## การติดตั้ง (Installation)

1. โคลนโปรเจคนี้:

```bash
git clone https://github.com/yourusername/thai-food-chatbot.git
cd thai-food-chatbot
```

2. สร้างและเปิดใช้งาน virtual environment:

```bash
# สำหรับ Windows
python -m venv venv
venv\Scripts\activate

# สำหรับ macOS และ Linux
python -m venv venv
source venv/bin/activate
```

3. ติดตั้งแพ็คเกจที่จำเป็น:

```bash
pip install -r requirements.txt
```

4. ตรวจสอบให้แน่ใจว่าไฟล์ `thai_food_processed.csv` อยู่ในโฟลเดอร์โปรเจค

## การใช้งาน (Usage)

1. เริ่มต้นแอปพลิเคชัน Streamlit:

```bash
streamlit run app.py
```

2. เปิดเว็บเบราว์เซอร์และไปที่ `http://localhost:8501`

3. พิมพ์คำถามเกี่ยวกับอาหารไทยหรือชื่ออาหารที่ต้องการในช่องแชท

## หมายเหตุทางเทคนิค (Technical Notes)

- โปรเจคนี้ใช้โมเดล `paraphrase-multilingual-MiniLM-L12-v2` สำหรับการสร้าง embeddings
- ในการเริ่มต้นครั้งแรก โมเดลจะถูกดาวน์โหลดและ embeddings จะถูกสร้างขึ้น ซึ่งอาจใช้เวลาสักครู่
- หลังจากการเริ่มต้นครั้งแรก โมเดลและ embeddings จะถูกบันทึกไว้เพื่อการใช้งานในอนาคตที่รวดเร็วขึ้น

## เริ่มต้นการฝึกอบรมใหม่ (Retraining)

หากคุณมีข้อมูลสูตรอาหารไทยใหม่ เพียงแค่อัปเดตไฟล์ `thai_food_processed.csv` และลบไฟล์ `embeddings.pkl` หากมี แอปพลิเคชันจะสร้าง embeddings ใหม่ในครั้งถัดไปที่เริ่มต้น

## โครงสร้างโปรเจค (Project Structure)

```
thai-food-chatbot/
├── app.py                # แอปพลิเคชัน Streamlit หลัก
├── requirements.txt      # รายการแพ็คเกจที่จำเป็น
├── README.md             # ไฟล์นี้
├── thai_food_processed.csv # ข้อมูลสูตรอาหารไทย
├── embeddings.pkl        # (สร้างโดยอัตโนมัติ) Embeddings ที่คำนวณไว้ล่วงหน้า
└── model/                # (สร้างโดยอัตโนมัติ) โฟลเดอร์ที่เก็บโมเดล Sentence Transformer
```

## ข้อกำหนด (Requirements)

- Python 3.7+
- Streamlit
- Sentence Transformers
- Pandas
- NumPy
- scikit-learn
- PyTorch
