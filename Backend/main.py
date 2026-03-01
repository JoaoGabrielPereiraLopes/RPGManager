from src.Global.Class.DatabaseConf import DB
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
import os

load_dotenv()

db=DB()
db.startDatabase()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("APP_HOST"),
        port=int(os.getenv("APP_PORT")),
        reload=True
    )