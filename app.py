import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def main():
    load_dotenv()
    st.set_page_config(page_title="ask your pdf")
    st.header("ask your PDF")

    pdf = st.file_uploader("upload your PDF", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        st.write(text)


if __name__ == "__main__":
    main()
