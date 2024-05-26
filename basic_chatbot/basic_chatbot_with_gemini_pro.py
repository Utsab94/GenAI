from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv("../environment.env")

os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user query."),
        ("user", "Question:{question}")
    ]
)

# Streamlit app
st.title("LangBot with Gemini-Pro")
input_text = st.text_input("Write your query here: ")

# Gemini integration
llm = ChatGoogleGenerativeAI(model="gemini-pro")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
