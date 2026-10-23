from insights import generate_insights

income = 8000

expenses = [
    {"amount": 1200, "type": "expense", "category": "Food"},
    {"amount": 500, "type": "expense", "category": "Transport"},
    {"amount": 750, "type": "expense", "category": "Education"},
    {"amount": 300, "type": "expense", "category": "Entertainment"}
]

results = generate_insights(income, expenses)

print("PennyWise AI Spending Insights")

for result in results:
    print("-", result)
