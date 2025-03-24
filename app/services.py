import os
from openai import OpenAI
import json
import numpy as np
from rank_bm25 import BM25Okapi

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def generate_embedding(text: str):
    try:
        response = client.embeddings.create(input=[text], model="text-embedding-3-small")
        return response["data"][0]["embedding"]
    except Exception as e:
        return {"error": "OpenAI API Error", "details": str(e)}

def retrieve_best_document(question: str, documents):
    corpus = [doc.content for doc in documents]
    tokenized_corpus = [doc.split() for doc in corpus]
    
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_question = question.split()
    scores = bm25.get_scores(tokenized_question)
    
    best_idx = int(np.argmax(scores))
    return documents[best_idx]
