import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

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
        
        # split into chunks
        text_spliter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function=len
        )

        chunks = text_spliter.split_text(text)

        st.write(chunks)


if __name__ == "__main__":
    main()
