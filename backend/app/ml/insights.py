def generate_insights(income, expenses):
    """Generate simple spending insights for students."""

    total_expenses = sum(
        item["amount"]
        for item in expenses
        if item["type"] == "expense"
    )

    balance = income - total_expenses
    insights = []

    if income <= 0:
        return ["Please enter a valid income to get insights."]

    if total_expenses > income:
        insights.append(
            "Warning: Your expenses exceed your income. "
            "Review your spending."
        )
    elif balance / income < 0.20:
        insights.append(
            "Your remaining balance is low. "
            "Try reducing non-essential expenses."
        )
    else:
        insights.append(
            "Your spending is within your income. "
            "Keep tracking your expenses."
        )

    category_totals = {}

    for item in expenses:
        if item["type"] == "expense":
            category = item.get("category", "Other")
            category_totals[category] = (
                category_totals.get(category, 0)
                + item["amount"]
            )

    if category_totals:
        highest_category = max(
            category_totals,
            key=category_totals.get
        )

        insights.append(
            f"Your highest-spending category is "
            f"{highest_category} "
            f"(₹{category_totals[highest_category]})."
        )

    return insights


def predict_monthly_expenses(monthly_expenses):
    """Estimate next month's expenses using past monthly totals."""

    if not monthly_expenses:
        return 0

    if any(amount < 0 for amount in monthly_expenses):
        raise ValueError("Expenses cannot be negative.")

    prediction = sum(monthly_expenses) / len(monthly_expenses)
    return round(prediction, 2)


def detect_unusual_spending(expenses):
    """Flag expenses more than twice their category average."""

    category_totals = {}

    for item in expenses:
        if item.get("type") != "expense":
            continue

        amount = item["amount"]

        if amount < 0:
            raise ValueError("Expenses cannot be negative.")

        category = item.get("category", "Other")
        category_totals.setdefault(category, []).append(amount)

    unusual = []

    for category, amounts in category_totals.items():
        average = sum(amounts) / len(amounts)

        if average <= 0:
            continue

        for amount in amounts:
            if amount > 2 * average:
                unusual.append({
                    "category": category,
                    "amount": amount,
                    "message": (
                        f"Unusually high spending in {category}: "
                        f"₹{amount}"
                    )
                })

    return unusual


def recommend_savings(income, expenses, savings_rate=0.20):
    """Suggest a savings target based on student income."""

    if income <= 0:
        return {
            "target": 0,
            "message": "Enter a valid income first."
        }

    if not 0 <= savings_rate <= 1:
        raise ValueError("Savings rate must be between 0 and 1.")

    total_expenses = sum(
        item["amount"]
        for item in expenses
        if item.get("type") == "expense"
    )

    if total_expenses < 0:
        raise ValueError("Expenses cannot be negative.")

    balance = income - total_expenses
    target = round(income * savings_rate, 2)

    if balance <= 0:
        message = "Review optional expenses and essential costs."
    elif balance < target:
        target = round(balance, 2)
        message = "Start with a smaller savings target that fits your budget."
    else:
        message = f"Try saving ₹{target:.2f} this month if affordable."

    return {
        "target": target,
        "message": message
    }

