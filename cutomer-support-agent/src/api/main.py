import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..rag.query import ask_question
from pydantic import BaseModel


app = FastAPI(
    title= "University Support AI Agent"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message" : "University Support AI Agent is Running...."} 

@app.post("/ask")
def ask(request: QuestionRequest):
    try:
        answer = ask_question(request.question)
        return {
            "success" : True,
            "question" : request.question,
            "answer" : answer
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
            }

if __name__ == "__main__":
    uvicorn.run("src.api.main:app", host="[0.0.0.0]", port=8000, reload=True)