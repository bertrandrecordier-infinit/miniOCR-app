import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

st.title("Mini OCR App")

# Upload image or PDF
uploaded_file = st.file_uploader("Upload an image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    # If the file is a PDF
    if uploaded_file.type == "application/pdf":
        pages = convert_from_bytes(uploaded_file.read())
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page) + "\n"
    else:
        # If the file is an image
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)

    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=300)