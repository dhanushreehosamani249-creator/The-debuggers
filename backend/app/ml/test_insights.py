
import unittest

from insights import (
    generate_insights,
    predict_monthly_expenses,
    detect_unusual_spending,
    recommend_savings,
)


class TestInsights(unittest.TestCase):

    def setUp(self):
        self.income = 8000
        self.expenses = [
            {"amount": 1200, "type": "expense", "category": "Food"},
            {"amount": 500, "type": "expense", "category": "Transport"},
            {"amount": 750, "type": "expense", "category": "Education"},
            {"amount": 300, "type": "expense", "category": "Entertainment"},
        ]

    def test_generate_insights(self):
        result = generate_insights(self.income, self.expenses)
        self.assertTrue(len(result) > 0)

    def test_monthly_prediction(self):
        result = predict_monthly_expenses([2000, 3000, 4000])
        self.assertEqual(result, 3000)

    def test_empty_prediction(self):
        self.assertEqual(predict_monthly_expenses([]), 0)

    def test_unusual_spending(self):
        expenses = [
            {"amount": 100, "type": "expense", "category": "Food"},
            {"amount": 100, "type": "expense", "category": "Food"},
            {"amount": 500, "type": "expense", "category": "Food"},
        ]
        result = detect_unusual_spending(expenses)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 500)

    def test_savings_recommendation(self):
        result = recommend_savings(10000, [
            {"amount": 6000, "type": "expense", "category": "Food"}
        ])
        self.assertEqual(result["target"], 2000)

    def test_invalid_income(self):
        result = recommend_savings(0, [])
        self.assertEqual(result["target"], 0)


if __name__ == "__main__":
    unittest.main()
