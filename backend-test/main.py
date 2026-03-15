from fastapi import FastAPI, Depends
from database import engine
from sqlalchemy.orm import Session

import models
import crud
import schemas
from database import SessionLocal, engine

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Expense tracker api running"}

@app.get("/home")
def home():
    return {"message":"Expense tracker api running"}