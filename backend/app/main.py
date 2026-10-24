from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
title="PennyWise API",
description="Backend for the student finance management app",
version="1.0.0"
)

class Expense(BaseModel):
amount: float
category: str
description: str = ""

expenses: List[Expense] = []

@app.get("/")
def home():
return {
"message": "Welcome to PennyWise API",
"status": "running"
}

@app.get("/health")
def health():
return {"status": "healthy"}

@app.post("/expenses")
def add_expense(expense: Expense):
if expense.amount <= 0:
return {"error": "Amount must be greater than zero"}

expenses.append(expense)

return {
    "message": "Expense added successfully",
    "expense": expense
}

@app.get("/expenses")
def get_expenses():
return {
"total_expenses": len(expenses),
"expenses": expenses
}
