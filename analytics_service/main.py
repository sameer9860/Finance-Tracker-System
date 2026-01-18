from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
from schemas import AnalyticsResponse


app = FastAPI(title="Finance Analytics Service")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/analytics/category-spending")
def category_spending(user_id: int, db: Session = Depends(get_db)):
    return crud.category_wise_spending(db, user_id)

@app.get("/analytics/income-vs-expense")
def income_expense(user_id: int, db: Session = Depends(get_db)):
    return crud.income_vs_expense(db, user_id)

@app.get("/analytics/category-spending", response_model=AnalyticsResponse)
def category_spending(user_id: int, db: Session = Depends(get_db)):
    return crud.category_wise_spending(db, user_id)
