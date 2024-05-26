import uvicorn
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
# from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import streamlit as st
from langserve import add_routes

load_dotenv("../environment.env")

os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A demo API"
)

# add_routes(
#     app,
#     ChatGoogleGenerativeAI(),
#     path="/gemini"
# )

# Prompt Template
prompt = ChatPromptTemplate.from_template("You are a helpful assistant. Please response to the {query}.")

# Streamlit app
st.title("LangBot with Gemini-Pro")
input_text = st.text_input("Write your query here: ")

# Gemini integration
llm = ChatGoogleGenerativeAI(model="gemini-pro")
# output_parser = StrOutputParser()

llm_local = Ollama(model="gemma:2b")

add_routes(
    app,
    prompt | llm,
    path="/askgemini"
)

add_routes(
    app,
    prompt | llm_local,
    path="/askgemma"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
