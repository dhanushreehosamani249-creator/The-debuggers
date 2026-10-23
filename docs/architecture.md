PennyWise AI — System Architecture

1. Overview

PennyWise AI is a student finance management application that combines a frontend, backend, database, and AI-based financial analysis.

2. System Components

Frontend — Member 1

- Displays the dashboard.
- Accepts income and expense entries.
- Displays budgets, charts, and savings goals.
- Shows AI insights and expense forecasts.

Backend — Member 2

- Receives requests from the frontend.
- Validates transaction data.
- Processes financial calculations.
- Communicates with the database.

AI/ML Module — Member 3

- Analyzes spending patterns.
- Estimates end-of-month expenses.
- Generates savings recommendations.

Integration and Testing — Member 4

- Coordinates integration of all components.
- Checks API communication.
- Tests complete application workflows.
- Prepares the final demonstration.

3. Application Workflow

1. A student enters income or expense information.
2. The frontend sends the information to the backend.
3. The backend validates and stores the transaction.
4. The backend retrieves financial data for calculations.
5. The AI/ML module analyzes available transactions.
6. The application displays updated balances, forecasts, and recommendations.

4. Technologies

- Frontend: React and Vite
- Backend: Python and FastAPI
- Database: PostgreSQL / Supabase
- Data analysis: Pandas and scikit-learn
- Version control: Git and GitHub

These technologies represent the planned architecture and should be updated if the implementation changes.

5. Integration Goal

The goal is to combine all components into one application where students can record transactions, monitor budgets, view spending forecasts, and track savings goals.
