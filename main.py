# Data Ingestion
import streamlit as st
#web based loader
from langchain_community.document_loaders import WebBaseLoader
import bs4
import tempfile
from io import BytesIO
st.info("web page loader and pdf loader")
st.header("Web page loader")
web_url=st.text_input("Enter the web page url")
# web_loader = WebBaseLoader(web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/"),
#                            bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-title", "post-content", "post-header"))))
if web_url:
    try:
        web_loader = WebBaseLoader(web_path=(web_url),verify_ssl=False,
                bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-title", "post-content", "post-header"))))

        llm_agents_web_article_data = web_loader.load()
        st.success("Web page loaded sucessfully")
        st.write(llm_agents_web_article_data)
    except Exception as e:
        st.error(f"Error: {e}")

# PDF loader
st.header("PDF loader")
from langchain_community.document_loaders import PyPDFLoader
#path=r'C:\Users\MQ955SE\Downloads\Python-Time-Series-Forecasting (1)\Python - Time Series Forecasting\Time Series Analysis\ARIMA, SARIMA and SARIMAX\SARIMAX Cheat Sheet.pdf'
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_file_path = tmp_file.name
    # bytes_io = BytesIO(uploaded_file.read())
    # st.write('came here')
    # st.write(bytes_io)
    pdf_loader = PyPDFLoader(temp_file_path)
    pdf_documents = pdf_loader.load()
    st.success("Pdf document loaded sucessfully")
    st.write(pdf_documents)
    # st.experimental_rerun()
# pdf_loader = PyPDFLoader("attention-is-all-you-need.pdf",)
# aiayn_documents = pdf_loader.load()
# print("Pdf document loaded sucessfully")
# print(aiayn_documents)
