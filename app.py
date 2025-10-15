import streamlit as st
from PIL import Image
import pytesseract
import fitz  # PyMuPDF — lightweight PDF library

st.title("Mini OCR App (Image + PDF)")

uploaded_file = st.file_uploader("Upload an image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    text = ""

    if uploaded_file.type == "application/pdf":
        # Use PyMuPDF to read each PDF page as an image
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page_num, page in enumerate(pdf_document):
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += f"\n--- Page {page_num + 1} ---\n"
            text += pytesseract.image_to_string(img)
        pdf_document.close()
    else:
        # Handle image uploads
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)

    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=300)
