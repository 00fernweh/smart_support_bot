from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET-Endpunkt für die Startseite
@app.get("/")
def read_root():
    return {"message": "Willkommen bei der Smart Support Bot API!"}

# Datenmodell für die Anfrage
class Question(BaseModel):
    question: str

# POST-Endpunkt zur Annahme von Benutzerfragen
@app.post("/ask")
def ask_question(item: Question):
    return {"response": f"Frage empfangen: '{item.question}'"}
