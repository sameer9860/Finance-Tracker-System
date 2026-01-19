from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
from schemas import AnalyticsResponse


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Finance Analytics Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
@app.get("/analytics/budget-status")
def budget_status(user_id: int, month: str, db: Session = Depends(get_db)):
    return crud.get_budget_status(db, user_id, month)

@app.get("/analytics/monthly-summary")
def monthly_summary(user_id: int, month: str, db: Session = Depends(get_db)):
    # month format: 'YYYY-MM'
    return crud.monthly_summary(db, user_id, month)
