# Convert RAG → Simple Agent.

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate

from langchain.agents import create_agent

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
# -------------------------
# STEP 1: Documents
# -------------------------
from common_setup import documents as docs

# -------------------------
# STEP 2: Vector Store
# -------------------------
# TODO: Create a splitter using the RecursiveCharacterTextSplitter()
# with a chunk size of 200 and chunk overlap of 0.
# Use variable name "splitter". 


# TODO: Create chunks by splitting the documents using the splitter.
# Use variable name "chunks". 


embeddings = OpenAIEmbeddings()

# TODO: Create the FAISS vector store using the chunks and embeddings generated above.
# Use variable name "vectorstore". 


# TODO: Create the retriever for the vector store.
# Use "k" value as 2.
# Use variable name "retriever". 
 

# -------------------------
# STEP 3: Tool
# @tool decorator.
# -------------------------
# TODO: apply the tool decorator.
def rag_search(query: str) -> str:
    """Search company policies"""
    print(f"\n Tool: rag_search()...")
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant information found."
    return "\n".join([d.page_content for d in docs])


# -------------------------
# STEP 4: LLM
# -------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# -------------------------
# STEP 5: CREATE AGENT
# -------------------------
# TODO: Create the agent assigning the model, tools and strict system prompt.
# Use variable name "agent".

# -------------------------
# CHATBOT LOOP
# -------------------------
if __name__ == "__main__":
    print("=== RAG Agent Chatbot ===")
    print("Type 'exit' to quit\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        response = agent.invoke({"messages": [{"role": "user", "content": query}]})

        print("Bot:", response["messages"][-1].content)
        
# What is leave policy?
# Travel reimbursement limit?
# How many leave days?
# GDP of France?
