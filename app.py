import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OllamaEmbeddings
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please respond to the question ansked."),
        ("user","Question: {question}")
    ]
)

## streamlit framework 
st.title("Langchain Demo with Gemma 2")
input_text = st.text_input("what question you have in mind?")

## Ollama Gemma 2 model
llm = OllamaLLM(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))