import streamlit as st
from PIL import Image
import fitz  # PyMuPDF for PDFs
import easyocr
import numpy as np

st.title("Mini OCR App (EasyOCR - Image + PDF)")

uploaded_file = st.file_uploader("Upload an image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    reader = easyocr.Reader(["en"])  # Initialize OCR reader (English)
    text = ""

    if uploaded_file.type == "application/pdf":
        # Read PDF pages as images
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page_num, page in enumerate(pdf_document):
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            np_img = np.array(img)
            results = reader.readtext(np_img, detail=0)
            text += f"\n--- Page {page_num + 1} ---\n" + "\n".join(results)
        pdf_document.close()
    else:
        # Handle image uploads
        image = Image.open(uploaded_file)
        np_img = np.array(image)
        results = reader.readtext(np_img, detail=0)
        text = "\n".join(results)

    st.subheader("Extracted Text")
    st.text_area("Text Output_
