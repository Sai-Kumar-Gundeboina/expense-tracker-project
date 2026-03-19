import models
from sqlalchemy.orm import Session
from security import hash_password
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    hash_pwd = hash_password(user.password)
    new_user = models.User(
        name = user.name,
        email = user.email,
        password = hash_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user_by_email(db: Session, email:str):
    return db.query(models.User).filter(models.User.email== email).first()

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    new_expense = models.Expense(
        amount=expense.amount,
        description=expense.description,
        category_id=expense.category_id,
        user_id=expense.user_id,
        expense_date=expense.expense_date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

def get_expense_by_user(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.user_id == user_id).all()

def delete_expense(db: Session, expense_id: int):
    expense = db.query(models.Expense).filter(models.Expense.expense_id == expense_id).first()

    if expense:
        db.delete(expense)
        db.commit()

    return expense

def update_expense(db: Session, expense_id: int, amount: float):
    expense = db.query(models.Expense).filter(models.Expense.expense_id == expense_id).first()

    if expense:
        expense.amount = amount
        db.commit()
        db.refresh(expense)
        
    return expense
def create_category(db: Session, category_name: str):
    new_category = models.Category(
        name = category_name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def get_category_by_id(db:Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()
