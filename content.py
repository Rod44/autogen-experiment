import os
from autogen import config_list_from_json
import autogen

import requests
from bs4 import BeautifulSoup
import json

from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate

import openai
from dotenv import load_dotenv

# Get API key
load_dotenv()
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define research function

def search(query):
    url = "https://www.google.com/search?q=" + query
    payload = json.dumps({
        "q": query
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.json()

