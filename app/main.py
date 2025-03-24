from fastapi import FastAPI
from .routes import document, qa

app = FastAPI(title="Document Management & RAG-based Q&A API")

# Include the document and Q&A routes with their prefixes
app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(qa.router, prefix="/qa", tags=["Q&A"])

@app.get("/")
async def root():
    return {"message": "Welcome to Document Management & RAG-based Q&A API"}
