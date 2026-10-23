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
