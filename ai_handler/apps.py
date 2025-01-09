from django.apps import AppConfig
import os
import requests
import bs4
import pandas as pd
import json
from langchain import hub
from langchain.schema import Document
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI



class AI_HandlerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ai_handler"
    
    def ready(self):
        dataset = pd.read_csv("D:\\document\\Hackaton\\money_in_this_economy_backend\\ai_handler\\news_articles.csv")
        dataset_json = dataset.to_json(orient='records')
        articles = json.loads(dataset_json)
        documents = [
                Document(page_content=json.dumps(article))  # Ensure each article is passed as JSON string
                for article in articles
            ]
        vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())
        self.retriever = vectorstore.as_retriever(search_type="similarity", top_k=5)
        
        