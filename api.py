from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Merhaba! Smart Support Bot API'sine hos geldiniz."}

# Veri modeli
class Question(BaseModel):
    question: str

# Yeni POST endpoint
@app.post("/ask")
def ask_question(item: Question):
    return {"response": f"Sorunuz alindi: '{item.question}'"}
