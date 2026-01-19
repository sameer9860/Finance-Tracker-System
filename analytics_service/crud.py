from sqlalchemy import text

def category_wise_spending(db, user_id: int):
    query = text("""
        SELECT category, SUM(amount) AS total
        FROM transactions_transaction
        WHERE user_id = :user_id
        AND transaction_type = 'expense'
        GROUP BY category
    """)
    result = db.execute(query, {"user_id": user_id}).fetchall()

    return {
        "labels": [row[0] for row in result],
        "values": [float(row[1]) for row in result],
    }


def income_vs_expense(db, user_id: int):
    query = text("""
        SELECT transaction_type, SUM(amount) AS total
        FROM transactions_transaction
        WHERE user_id = :user_id
        GROUP BY transaction_type
    """)
    result = db.execute(query, {"user_id": user_id}).fetchall()

    return {
        "labels": [row[0] for row in result],
        "values": [float(row[1]) for row in result],
    }
def get_budget_status(db, user_id: int, month: str):
    # month format should be 'YYYY-MM-DD' (first day of the month)
    # 1. Get Budgets
    budget_query = text("""
        SELECT id, category, amount_limit
        FROM budgets_budget
        WHERE user_id = :user_id AND month = :month
    """)
    budgets = db.execute(budget_query, {"user_id": user_id, "month": month}).fetchall()

    # 2. Get Expenses for the same month and user
    # Extract year and month for transaction filtering
    year_month = month[:7] # 'YYYY-MM'
    
    expense_query = text("""
        SELECT category, SUM(amount) AS total
        FROM transactions_transaction
        WHERE user_id = :user_id 
        AND transaction_type = 'expense'
        AND strftime('%Y-%m', date) = :year_month
        GROUP BY category
    """)
    expenses = db.execute(expense_query, {"user_id": user_id, "year_month": year_month}).fetchall()
    
    # Map expenses by category
    expense_map = {row[0]: float(row[1]) for row in expenses}
    
    result = []
    for b in budgets:
        spent = expense_map.get(b[1], 0.0)
        result.append({
            "id": b[0],
            "category": b[1],
            "limit": float(b[2]),
            "spent": spent,
            "remaining": max(0, float(b[2]) - spent),
            "overspent": spent > float(b[2])
        })
    
    return result

def monthly_summary(db, user_id: int, month: str):
    # month format: 'YYYY-MM'
    query = text("""
        SELECT transaction_type, SUM(amount) AS total
        FROM transactions_transaction
        WHERE user_id = :user_id
        AND strftime('%Y-%m', date) = :month
        GROUP BY transaction_type
    """)
    result = db.execute(query, {"user_id": user_id, "month": month}).fetchall()
    
    summary = {"income": 0.0, "expense": 0.0, "balance": 0.0}
    for row in result:
        if row[0] == 'income':
            summary["income"] = float(row[1])
        else:
            summary["expense"] = float(row[1])
    
    summary["balance"] = summary["income"] - summary["expense"]
    return summary
