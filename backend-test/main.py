from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Expense tracker api running"}

@app.get("/home")
def home():
    return {"message":"Expense tracker api running"}