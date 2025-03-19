import pandas as pd
import re
import os
import argparse

def clean_text(text):
    """Clean and format text data"""
    if not isinstance(text, str):
        return ""
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters except Thai characters, numbers and basic punctuation
    text = re.sub(r'[^\u0E00-\u0E7Fa-zA-Z0-9\s.,\-\(\)]', '', text)
    
    return text.strip()

def preprocess_ingredients(text):
    """Format ingredient lists"""
    if not isinstance(text, str):
        return ""
    
    # Make sure each ingredient is on a new line and starts with a dash
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Ensure each line starts with a dash
        if not line.startswith('-'):
            line = f"- {line}"
        
        formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def preprocess_data(input_file, output_file):
    """Preprocess the Thai food dataset"""
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return False
    
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Check required columns
        required_columns = ['name', 'text_ingradiant', 'food_method']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Error: Missing required columns: {', '.join(missing_columns)}")
            return False
        
        # Clean text in each column
        df['name'] = df['name'].apply(clean_text)
        df['food_method'] = df['food_method'].apply(clean_text)
        df['text_ingradiant'] = df['text_ingradiant'].apply(preprocess_ingredients)
        
        # Remove duplicates
        df = df.drop_duplicates(subset=['name'])
        
        # Reset index
        df = df.reset_index(drop=True)
        
        # Save preprocessed data
        df.to_csv(output_file, index=False)
        
        print(f"Preprocessing completed. Saved to '{output_file}'")
        print(f"Total recipes: {len(df)}")
        
        # If embeddings file exists, remove it so it will be regenerated
        if os.path.exists('embeddings.pkl'):
            os.remove('embeddings.pkl')
            print("Removed existing embeddings file. It will be regenerated when the app runs.")
        
        return True
    
    except Exception as e:
        print(f"Error during preprocessing: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess Thai food recipe data')
    parser.add_argument('--input', type=str, default='thai_food_raw.csv', 
                        help='Input CSV file path')
    parser.add_argument('--output', type=str, default='thai_food_processed.csv', 
                        help='Output CSV file path')
    
    args = parser.parse_args()
    preprocess_data(args.input, args.output)
