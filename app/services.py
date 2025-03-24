import os
import openai
import json
import numpy as np
from rank_bm25 import BM25Okapi

# Set OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_embedding(text: str):
    response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

def retrieve_best_document(question: str, documents):
    # Create a corpus using the content of each document
    corpus = [doc.content for doc in documents]
    tokenized_corpus = [doc.split() for doc in corpus]
    
    # Use BM25 to score each document based on the question
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_question = question.split()
    scores = bm25.get_scores(tokenized_question)
    
    best_idx = int(np.argmax(scores))
    return documents[best_idx]
