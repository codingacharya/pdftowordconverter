import streamlit as st
from pdf2docx import Converter
import os

def convert_pdf_to_word(pdf_file, output_file):
    cv = Converter(pdf_file)
    cv.convert(output_file, start=0, end=None)
    cv.close()

def main():
    st.title("PDF to Word Converter")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        
        output_file = "converted.docx"
        
        if st.button("Convert to Word"):
            with st.spinner("Converting..."):
                convert_pdf_to_word(uploaded_file, output_file)
            st.success("Conversion successful!")
            
            with open(output_file, "rb") as f:
                st.download_button(label="Download Word File",
                                   data=f,
                                   file_name="converted.docx",
                                   mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            
            os.remove(output_file)  # Cleanup after download

if __name__ == "__main__":
    main()