from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import QuestionRequest, AnswerResponse
from ..crud import get_all_documents
from ..services import retrieve_best_document
from langchain.llms import OpenAI

router = APIRouter()
llm = OpenAI()  # Initialize the LangChain OpenAI wrapper

@router.post("/", response_model=AnswerResponse)
async def get_answer(question: QuestionRequest, db: Session = Depends(get_db)):
    docs = get_all_documents(db)
    if not docs:
        return {"answer": "No documents available.", "document": ""}
    best_doc = retrieve_best_document(question.question, docs)
    
    # Generate answer based on the best matching document's content
    answer = llm(question=question.question, context=best_doc.content)
    return {"answer": answer, "document": best_doc.title}
