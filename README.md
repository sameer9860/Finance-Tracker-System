# 💰 Finance Tracker System – Installation & Setup Guide

A full-stack **Finance Tracker System** built with **Django**, **React**, and **FastAPI** to track expenses, manage budgets, and view financial analytics.

---

## 📌 Prerequisites

Before starting, ensure you have the following installed:

* Python **3.10+**
* Node.js **18+** and npm
* Git
* Virtual environment support

---

## 🖼️ Application Screenshots

All screenshots are stored in:

```
finance-frontend/src/assets/
```

---

### 📊 Dashboard

![Dashboard](finance-frontend/src/assets/dashboard.png)
![Dashboard](finance-frontend/src/assets/dashboard2.png)

---

### 💸 Budgets

![Budgets](finance-frontend/src/assets/budgets.png)

---

### 📑 Transactions

![Transactions](finance-frontend/src/assets/transaction.png)

---

### ⚙️ Settings

![Settings](finance-frontend/src/assets/settings.png)

---

## 🔹 Installation Guide

---

## 🔸 Backend Setup (Django)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sameer9860/Finance-Tracker-System.git

cd finance_tracker_project
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

---

### 3️⃣ Activate Virtual Environment

**Windows (PowerShell)**

```powershell
.\env\Scripts\activate
```

**Windows (CMD)**

```cmd
env\Scripts\activate
```

**macOS / Linux**

```bash
source env/bin/activate
```

---

### 4️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

👉 Follow the prompts to create an admin account.

---

### 7️⃣ Run Django Development Server

```bash
python manage.py runserver
```

🌐 Django Backend URL:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔸 Analytics Service Setup (FastAPI)

### 8️⃣ Navigate to Analytics Service

```bash
cd analytics_service
```

---

### 9️⃣ Install Analytics Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔟 Run FastAPI Server

```bash
uvicorn main:app --reload --port 8001
```

🌐 FastAPI Analytics URL:
**[http://127.0.0.1:8001/](http://127.0.0.1:8001/)**

---

## 🔸 Frontend Setup (React)

### 1️⃣1️⃣ Navigate to React Frontend

```bash
cd finance-frontend
```

---

### 1️⃣2️⃣ Install Frontend Dependencies

```bash
npm install
```

---

### 1️⃣3️⃣ Start React Development Server

```bash
npm start
```

🌐 React Frontend URL:
**[http://localhost:3000/](http://localhost:3000/)**

---

## ✅ Features

* User Authentication
* Expense & Income Tracking
* Budget Management
* Transaction History
* Analytics & Insights (FastAPI)
* Admin Panel
* Responsive Dashboard UI

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Analytics:** FastAPI
* **Frontend:** React, npm
* **Database:** SQLite / PostgreSQL
* **Version Control:** Git & GitHub

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

⭐ If you like this project, don’t forget to give it a star on GitHub!
