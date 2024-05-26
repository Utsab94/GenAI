from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv("../environment.env")

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
st.title("LangBot with Gemma open source")
input_text = st.text_input("Write your query here: ")

# Gemini integration
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

