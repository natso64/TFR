def search_dish(query, df):
    """ค้นหาเมนูที่เกี่ยวข้องกับคำถาม"""
    results = df[df['ชื่อเมนู'].str.contains(query, case=False, na=False)]
    return results

def recommend_dishes(ingredients, df):
    """แนะนำเมนูตามวัตถุดิบที่ป้อน"""
    filtered_df = df[df['ส่วนผสม'].apply(lambda x: all(ing in str(x) for ing in ingredients))]
    return filtered_df
