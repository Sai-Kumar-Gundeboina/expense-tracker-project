from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    password: str
    email: str

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

class ExpenseCreate(BaseModel):
    amount: float
    description: str
    category_id: int
    user_id: int
    expense_date: date

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    description: str
    category_id: int
    user_id: int
    expense_date: date

class ExpenseUpdate(BaseModel):
    amount: float