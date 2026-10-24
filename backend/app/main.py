
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from app.ml.insights import (
    generate_insights,
    predict_monthly_expenses,
    detect_unusual_spending,
    recommend_savings,
)

app = FastAPI(
    title="PennyWise API",
    description="AI-powered student finance management backend",
    version="1.0.0",
)


# Expense data model
class Expense(BaseModel):
    amount: float = Field(gt=0, description="Expense amount must be positive")
    category: str = Field(min_length=1, description="Expense category")
    description: str = ""


# Temporary in-memory storage
expenses: List[Expense] = []


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to PennyWise API",
        "status": "running",
    }


# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}


# Add an expense
@app.post("/expenses")
def add_expense(expense: Expense):
    expenses.append(expense)

    return {
        "message": "Expense added successfully",
        "expense": expense,
    }


# Get all expenses
@app.get("/expenses")
def get_expenses():
    return {
        "total_expenses": len(expenses),
        "total_amount": sum(item.amount for item in expenses),
        "expenses": expenses,
    }


# Generate AI spending insights
@app.get("/ai/insights")
def ai_insights(income: float = Field(gt=0)):
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


# Predict monthly expenses
@app.get("/ai/predict")
def ai_predict():
    if not expenses:
        return {
            "predicted_expenses": 0,
            "message": "Add expenses to generate a prediction.",
        }

    # Current total is a baseline, not a historical forecast.
    monthly_totals = [
        sum(item.amount for item in expenses)
    ]

    prediction = predict_monthly_expenses(monthly_totals)

    return {
        "predicted_expenses": prediction,
        "based_on": "Current recorded expenses",
        "note": "A reliable monthly forecast needs dated expenses from multiple months.",
    }


# Detect unusual spending
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
        "unusual_spending": detect_unusual_spending(expense_data)
    }


# Recommend savings
@app.get("/ai/savings")
def ai_savings(income: float = Field(gt=0)):
    expense_data = [
        {
            "amount": item.amount,
            "type": "expense",
            "category": item.category,
        }
        for item in expenses
    ]

    return {
        "recommendations": recommend_savings(income, expense_data)
    }
