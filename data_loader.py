import pandas as pd

def load_data():
    """โหลดข้อมูลจากไฟล์ Excel"""
    file_path = "thai_food_processed.xlsx"
    df = pd.read_excel(file_path)
    return df
