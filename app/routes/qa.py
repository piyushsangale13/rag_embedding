from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from openai import OpenAIError
from ..database import get_db
from ..schemas import QuestionRequest, AnswerResponse
from ..crud import get_all_documents
from ..services import retrieve_best_document
from langchain.llms import OpenAI

router = APIRouter()
llm = OpenAI() 

@router.post("/", response_model=AnswerResponse)
async def get_answer(question: QuestionRequest, db: Session = Depends(get_db)):
    docs = get_all_documents(db)
    if not docs:
        return {"answer": "No documents available.", "document": ""}

    best_doc = retrieve_best_document(question.question, docs)
    prompt = f"Context: {best_doc.content}\n\nQuestion: {question.question}\nAnswer:"

    try:
        answer = llm.invoke(prompt)
    except OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    return {"answer": answer, "document": best_doc.title}
