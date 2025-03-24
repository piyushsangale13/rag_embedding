from pydantic import BaseModel

class DocumentUpload(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    document: str
