from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Smart Support Bot API is working!"}

@app.get("/faq")
def get_faq():
    with open("faq_data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {"faq": [line.strip() for line in lines if line.strip()]}

