import streamlit as st
import pandas as pd
from data_loader import load_data
from chatbot import search_dish, recommend_dishes

def main():
    """แอปหลัก"""
    st.title("แชทบอทอาหารไทย 🍜")
    df = load_data()

    # โหมดการใช้งาน
    option = st.radio("เลือกโหมดการใช้งาน", ["ถามเกี่ยวกับเมนู", "แนะนำเมนูจากวัตถุดิบ"])

    if option == "ถามเกี่ยวกับเมนู":
        query = st.text_input("ป้อนชื่อเมนูที่ต้องการสอบถาม:")
        if st.button("ค้นหา"):
            results = search_dish(query, df)
            if not results.empty:
                for _, row in results.iterrows():
                    st.subheader(row['ชื่อเมนู'])
                    st.write(f"**ส่วนผสม:** {row['ส่วนผสม']}")
                    st.write(f"**วิธีทำ:** {row['วิธีทำ']}")
            else:
                st.write("ไม่พบเมนูที่ค้นหา")

    elif option == "แนะนำเมนูจากวัตถุดิบ":
        ingredients = st.text_input("ป้อนวัตถุดิบที่คุณมี (คั่นด้วยเครื่องหมายจุลภาค):")
        if st.button("แนะนำเมนู"):
            ingredient_list = [ing.strip() for ing in ingredients.split(",")]
            recommendations = recommend_dishes(ingredient_list, df)
            if not recommendations.empty:
                for _, row in recommendations.iterrows():
                    st.subheader(row['ชื่อเมนู'])
                    st.write(f"**ส่วนผสม:** {row['ส่วนผสม']}")
                    st.write(f"**วิธีทำ:** {row['วิธีทำ']}")
            else:
                st.write("ไม่พบเมนูที่สามารถทำได้")

if __name__ == "__main__":
    main()
