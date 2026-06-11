# Multi-Step Chatbot.

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from common_setup import documents as docs

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
# --------------------------------------------------
# VECTOR STORE
# --------------------------------------------------

# TODO: Create a splitter using the RecursiveCharacterTextSplitter()
# with a chunk size of 300 and chunk overlap of 50.
# Use variable name "splitter". 


# TODO: Create chunks by splitting the documents using the splitter.
# Use variable name "chunks". 


embeddings = OpenAIEmbeddings()

# TODO: Create the FAISS vector store using the chunks and embeddings generated above.
# Use variable name "vectorstore". 


# TODO: Create the retriever for the vector store.
# Use "k" value as 3.
# Use variable name "retriever". 
 


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# --------------------------------------------------
# STEP 1: INTENT DETECTION
# --------------------------------------------------

def detect_intent(query: str):
    # TODO: Create a prompt to classify the given query into one of these categories:
    # - Leave
    # - Travel
    # - Reimbursement
    # - Calculation
    # - Other
    # Pass the query as a placeholder.
    # Return only the category.
    # Use the variable name "prompt"


    return llm.invoke(prompt).content.strip()

# --------------------------------------------------
# STEP 2: RETRIEVE
# --------------------------------------------------

def retrieve(query: str):

    docs = retriever.invoke(query)

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    return context

# --------------------------------------------------
# STEP 3: QUALITY CHECK
# --------------------------------------------------

def context_is_relevant(query, context):

    prompt = f"""
Question:
{query}

Context:
{context}

Does the context contain enough information
to answer the question?

Answer ONLY:
YES
or
NO
"""

    result = llm.invoke(prompt).content.strip().upper()

    return "YES" in result

# --------------------------------------------------
# STEP 4: QUERY REWRITE
# --------------------------------------------------

def rewrite_query(query):

    prompt = f"""
Rewrite this query so that it is easier
for a company policy search engine
to understand.

Query:
{query}

Return only rewritten query.
"""

    return llm.invoke(prompt).content.strip()

# --------------------------------------------------
# STEP 5: GENERATE ANSWER
# --------------------------------------------------

def generate_answer(query, context):

    # TODO: Create a prompt to generate an answer for the provided query and context.
    # Pass both as place holders.
    # Instruct the LLM to answer only from the given context.
    # If the answer is not present, it should say "I don't know".
    # Use the variable name "prompt"


    return llm.invoke(prompt).content

# --------------------------------------------------
# STEP 6: VALIDATE ANSWER
# --------------------------------------------------

def validate_answer(query, context, answer):

    prompt = f"""
Question:
{query}

Context:
{context}

Answer:
{answer}

Determine which of the following applies:

1. SUPPORTED
   - The answer is directly supported by the context

2. UNSUPPORTED
   - The answer contains facts not present in the context

3. NOT_FOUND
   - The context does not contain enough information
     to answer the question

Return ONLY one word:
SUPPORTED
UNSUPPORTED
NOT_FOUND
"""

    return llm.invoke(prompt).content.strip()

# --------------------------------------------------
# MAIN WORKFLOW
# --------------------------------------------------

def run_workflow(query):

    # TODO: Create ghe workflow as follows:
    # Step 1: Detect the intention of the query.
    # Step 2: Retrieve the context for the given query.
    # Step 3: Check if the context is relevant.
    # If the context is not relevant, rewrite the query and retrieve the context again for the new query.
    # Step 4: Generate the answer.
    # Step 5: Validate the answer.
    # If the answer is not valid, reutnr "I could not find a reliable answer in the available policies."
    # If the answer is valid, return the answer.
    # Print the output of each step.

    print("\n========== STEP 1 - Intent Detection ==========")


    print("\n========== STEP 2 - Retrieve Context ==========")


    print("\n========== STEP 3 - Check Context Relevance ==========")

    # Retry Retrieval
    if not relevant:

        print("\n========== RETRY - Rewrite Query if not Relevant ==========")


    print("\n========== STEP 4 - Generate Answer ==========")


    print("\n========== STEP 5 - Validate Answer ==========")

    return answer

# --------------------------------------------------
# CHATBOT
# --------------------------------------------------

if __name__ == "__main__":

    print("\nBetter Multi-Step Workflow Demo")
    print("Type 'exit' to quit\n")

    while True:

        query = input("You: ")

        if query.lower() == "exit":
            break

        response = run_workflow(query)

        print("\nBot:", response)


# Intent Detection:
# How many leave days do employees get?
# What is the meal reimbursement limit?
# Can I work from home?
# How many days can i work from home?

# Retrieval Retry:
# Tell me about company spending
# What is the annual bonus percentage?
