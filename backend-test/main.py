from fastapi import FastAPI, Depends
from database import engine
from sqlalchemy.orm import Session
from security import verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

import models
import crud
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"Expense tracker api running"}

@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/login")
def login(
   user: schemas.UserLogin, 
    db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db, user.email)

    if not db_user:
        return {"message": "User not found"}
    
    if not verify_password(user.password, db_user.password):
        return {"message": "Invalid password"}
    
    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    # return {"message": "Login Successful", "user_id": db_user.id}
    
@app.post("/expense")
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

# @app.get("/expense/{user_id}")
# def get_expense_by_user(user_id: int, db: Session = Depends(get_db)):
#     return crud.get_expense_by_user(db, user_id)

@app.get("/expense")
def get_expense_by_user(user_id: int, db: Session = Depends(get_db)): #= Depends(get_current_user)
    return crud.get_expense_by_user(db, user_id)

@app.put("/expense/{expense_id}")
def update_expense(expense_id: int, expense: schemas.ExpenseUpdate, db: Session = Depends(get_db)):
    return crud.update_expense(db, expense_id, expense.amount)

@app.delete("/expense/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.delete_expense(db, expense_id)

@app.post("/category")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category.name)

@app.get("/category/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category_by_id(db, category_id)