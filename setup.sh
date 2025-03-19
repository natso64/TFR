#!/bin/bash

# Thai Food Recipe Chatbot Setup Script

echo "===== Thai Food Recipe Chatbot Setup ====="
echo "Setting up environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/macOS
    source venv/bin/activate
fi

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt

# Check if the dataset exists
if [ ! -f "thai_food_processed.csv" ]; then
    echo "Error: thai_food_processed.csv not found in the current directory."
    echo "Please make sure the data file is in the project directory."
    exit 1
fi

echo "Setup completed successfully!"
echo ""
echo "To run the chatbot, use the following command:"
echo "streamlit run app.py"
echo ""
echo "Thank you for using Thai Food Recipe Chatbot!"
