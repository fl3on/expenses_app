from fastapi import FastAPI, Depends, HTTPException
from models import Expense, Base
from schemas import ExpenseSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import pyodbc, struct

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def get_expense_welcome():
    return {"greeting":"Hello world"}

@app.get("/expense/{expense_id}")
async def get_expense(expense_id, db:Session=Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id==expense_id).first()

    return expense


@app.get("/types/{expense_type}-{price}")
async def get_expense_type_price(expense_type, price, db:Session=Depends(get_db)):
    expense = db.query(Expense).filter((Expense.expensetype==expense_type)&(Expense.price>price)).all()

    return expense


@app.get("/types/{expense_type}")
async def get_expense_type(expense_type, db:Session=Depends(get_db)):
    expense = db.query(Expense).filter(Expense.expensetype==expense_type).all()

    return expense