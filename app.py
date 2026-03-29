import streamlit as st
from pypdf import PdfReader
from transformers import pipeline

st.title("GenAI Business Report Summarizer")

uploaded_file = st.file_uploader("Upload a business report (PDF)", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""

    # read first 2 pages
    for page in reader.pages[:2]:
        text += page.extract_text()

    st.write("Generating summary...")

    # load AI model
    generator = pipeline("text-generation", model="google/flan-t5-base")

    # create prompt
    prompt = "Summarize this business report:\n" + text

    # generate summary
    result = generator(prompt, max_length=200)
# update
    summary = result[0]["generated_text"].replace("Summarize this business report:", "")

    st.subheader("Summary")
    st.write(summary)