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
