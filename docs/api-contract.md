PennyWise AI — API Contract

Purpose

This document defines the planned API endpoints for communication between the frontend and backend.

Base URL for local development:

"http://localhost:8000"

1. Add a Transaction

Method: POST

Endpoint: "/transactions"

Example request:

{
  "amount": 150,
  "type": "expense",
  "category": "Food",
  "description": "Lunch",
  "date": "2026-10-23"
}

Expected result: The transaction is validated and saved.

2. Retrieve Transactions

Method: GET

Endpoint: "/transactions"

Purpose: Retrieve the available transactions for the current user.

3. Retrieve Dashboard Information

Method: GET

Endpoint: "/dashboard"

Purpose: Retrieve the current balance, monthly income, monthly expenses and budget summaries.

4. Manage Budgets

Method: POST

Endpoint: "/budgets"

Purpose: Create or update a spending budget.

Method: GET

Endpoint: "/budgets"

Purpose: Retrieve budgets and their usage.

5. Manage Savings Goals

Method: POST

Endpoint: "/goals"

Purpose: Create a savings goal.

Method: GET

Endpoint: "/goals"

Purpose: Retrieve savings goals and their progress.

6. Retrieve AI Insights

Method: GET

Endpoint: "/insights"

Purpose: Retrieve spending analysis and personalized recommendations.

7. Retrieve Expense Forecast

Method: GET

Endpoint: "/forecast"

Purpose: Retrieve the estimated end-of-month expenses.

Integration Rules

1. Transaction amounts must be positive numbers.
2. The transaction type must be either "income" or "expense".
3. Dates use the "YYYY-MM-DD" format.
4. Currency is INR (₹).
5. The frontend and backend must agree on the request and response formats.
6. Forecasts must be identified as estimates.
7. These endpoints describe the planned API contract. They must not be considered implemented until the backend supports them.
