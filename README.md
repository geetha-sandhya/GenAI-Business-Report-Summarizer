# GenAI Business Report Summarizer

## Live Demo

https://genai-business-report-summarizer-8s4bsgjdsjqzhxns4po3ta.streamlit.app/


## Overview

The **GenAI Business Report Summarizer** is a Generative AI application that automatically analyzes and summarizes business reports from PDF documents. The system uses Natural Language Processing (NLP) techniques and open-source Large Language Models (LLMs) to extract important information and generate concise summaries that help users quickly understand long business documents.

This project demonstrates the use of **Generative AI, NLP pipelines, and document processing** to build an intelligent analytics assistant for business workflows.

---

## Problem Statement

Business reports such as annual reports, financial documents, and analytical summaries are often very long and time-consuming to read. Manually extracting key insights from these documents can be inefficient.

This project aims to solve this problem by building an AI system that can:

* Extract text from business reports
* Process and understand the content
* Generate meaningful summaries automatically

---

## Project Workflow

### 1. Environment Setup

The project environment was prepared by installing required Python libraries including:

* transformers
* streamlit
* pypdf
* pandas
* sentence-transformers
* faiss-cpu

These libraries support **document processing, NLP modeling, and web application deployment**.

---

### 2. Document Processing

The system reads PDF files using the **PyPDF library**.

Steps performed:

* Load the uploaded PDF file
* Extract text content from the document pages
* Prepare the extracted text for NLP processing

---

### 3. Generative AI Model Integration

The project integrates an open-source Large Language Model using **HuggingFace Transformers**.

Model used:

* `google/flan-t5-base`

The model processes the extracted document text and generates a summarized version of the content.

---

### 4. NLP Pipeline

The pipeline for the summarization process includes:

1. Input document upload
2. PDF text extraction
3. Text preprocessing
4. LLM-based summarization
5. Displaying the summarized output

This pipeline demonstrates a simple **Generative AI analytics workflow**.

---

### 5. Web Application Interface

To make the system interactive, a web application was developed using **Streamlit**.

Features of the interface:

* Upload business report PDFs
* Automatic text extraction
* AI-generated summary display
* Simple and user-friendly interface

---

## Technologies Used

* **Python**
* **Generative AI**
* **Natural Language Processing (NLP)**
* **HuggingFace Transformers**
* **PyPDF**
* **Streamlit**
* **FAISS (for future vector search extension)**

---

## Project Structure

project/

data/                # Sample PDF documents
app.py               # Main Streamlit application
requirements.txt     # Python dependencies
README.md            # Project documentation

---

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/your-username/GenAI-Business-Report-Summarizer

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Run the application

streamlit run app.py

---

### 4. Open the application

The application will run locally at:

http://localhost:8501

Upload a PDF document and the system will generate a summary automatically.

---

## Example Use Cases

* Business report analysis
* Financial document summarization
* Corporate report insights
* Automated document understanding

---

## Future Improvements

* Implement **Retrieval Augmented Generation (RAG)** architecture
* Add **question-answering over documents**
* Integrate **vector databases for document search**
* Support **multiple document formats**

---

## Author

Geetha Sandhya
B.Tech – Artificial Intelligence and Machine Learning
