import streamlit as st 
from langchain_xai import ChatXAI
import os 
from dotenv import load_dotenv
load_dotenv()


os.environ['x_api'] = os.getenv('x_api')

model = ChatXAI(model="grok-beta")

