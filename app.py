import streamlit as st
from pypdf import PdfReader
from transformers import pipeline

st.title("AI Business Report Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages[:2]:
        text += page.extract_text()

    generator = pipeline("text-generation", model="google/flan-t5-base")

    prompt = "Summarize this business report:\n" + text

    result = generator(prompt, max_length=150)

    st.subheader("Summary:")
    st.write(result[0]["generated_text"])