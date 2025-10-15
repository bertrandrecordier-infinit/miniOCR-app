import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

st.title("Mini OCR App")

uploaded_file = st.file_uploader("Upload an image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
if uploaded_file.type == "application/pdf":
# Convert PDF to images
pages = convert_from_bytes(uploaded_file.read())
text = ""
for page in pages:
text += pytesseract.image_to_string(page) + "\n"
else:
image = Image.open(uploaded_file)
text = pytesseract.image_to_string(image)

st.subheader("Extracted Text")
st.text_area("Text Output", text, height=300)