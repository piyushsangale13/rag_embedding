from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import DocumentUpload, DocumentResponse
from ..services import generate_embedding
from ..crud import create_document, get_all_documents

router = APIRouter()

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(doc: DocumentUpload, db: Session = Depends(get_db)):
    embedding = generate_embedding(doc.content)
    new_doc = create_document(db, doc.title, doc.content, embedding)
    return new_doc

@router.get("/", response_model=list[DocumentResponse])
async def list_documents(db: Session = Depends(get_db)):
    docs = get_all_documents(db)
    return docs
