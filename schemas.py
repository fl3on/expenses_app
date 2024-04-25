from pydantic import BaseModel
from datetime import date

class ExpenseSchema(BaseModel):
    id:int
    date:date
    concept: str
    price: float
    expensetype: str 