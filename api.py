from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Smart Support Bot API is working!"}
