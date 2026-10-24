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


from app.ml.insights import (
    generate_insights,
    predict_monthly_expenses,
    detect_unusual_spending,
    recommend_savings,
)


@app.get("/ai/insights")
def ai_insights(income: float):
    expense_data = [
        {
            "amount": item.amount,
            "type": "expense",
            "category": item.category,
        }
        for item in expenses
    ]

    return {
        "insights": generate_insights(income, expense_data)
    }


@app.get("/ai/predict")
def ai_predict():
    monthly_totals = [sum(item.amount for item in expenses)]
    return {
        "predicted_expenses": predict_monthly_expenses(
            monthly_totals
        )
    }


@app.get("/ai/unusual-spending")
def ai_unusual_spending():
    expense_data = [
        {
            "amount": item.amount,
            "type": "expense",
            "category": item.category,
        }
        for item in expenses
    ]

    return {
        "unusual_spending": detect_unusual_spending(
            expense_data
        )
    }

