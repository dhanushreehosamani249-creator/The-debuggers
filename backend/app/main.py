from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from app.ml.insights import generate_insights

app = FastAPI(title="PennyWise AI API")


class Transaction(BaseModel):
    amount: float
    type: str
    category: str
    description: Optional[str] = ""
    date: Optional[str] = ""


class InsightsRequest(BaseModel):
    income: float
    expenses: List[Transaction]


@app.get("/")
def home():
    return {
        "message": "Welcome to PennyWise AI",
        "status": "running"
    }


@app.post("/insights")
def get_insights(data: InsightsRequest):
    expenses = [
        item.model_dump()
        for item in data.expenses
    ]

    insights = generate_insights(
        data.income,
        expenses
    )

    return {"insights": insights}
