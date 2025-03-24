from sqlalchemy.orm import Session
from .models import Document
import json

def create_document(db: Session, title: str, content: str, embedding: list):
    new_doc = Document(title=title, content=content, embedding=json.dumps(embedding))
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def get_all_documents(db: Session):
    return db.query(Document).all()

def get_document_by_id(db: Session, doc_id: int):
    return db.query(Document).filter(Document.id == doc_id).first()
