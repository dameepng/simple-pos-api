# Simple POS API (FastAPI)
Simple Point of Sale (POS) Backend API built with FastAPI.
This project is intended as a backend portfolio, demonstrating clean architecture, database migrations, transactions, testing, and CI.

![CI](https://github.com/dameepng/simple-pos-api/actions/workflows/ci.yml/badge.svg)
## ✨ Features
- Products
  - Create product
  - List products with pagination (limit, offset)
  - Update stock

- Orders
  - Create order with multiple items
  - Automatic stock deduction
  - Transaction-safe processing

## 🧱 Architecture
This project follows Layered Architecture:
```bash
API (Routes)
   ↓
Service (Business Logic)
   ↓
Repository (Database Access)
   ↓
Database
```
Benefits:
- Clear separation of concerns
- Easier testing
- Scalable for future features

## 🛠 Tech Stack
- Python 3.12
- FastAPI – REST API framework
- SQLAlchemy – ORM & transaction handling
- Alembic – database migrations
- PostgreSQL – primary database (Docker)
- SQLite – test database
- Pytest – automated testing
- GitHub Actions – CI pipeline
- Docker Compose – local database environment

## 📁 Project Structure
```bash
app/
  main.py              # FastAPI entry point
  api/
    routes/            # HTTP endpoints (products, orders)
  core/
    money.py           # Decimal & money utilities
  db/
    session.py         # DB session & dependency
  models/              # SQLAlchemy ORM models
  repositories/        # Database access layer
  schemas/             # Pydantic request/response schemas
  services/            # Business logic layer
alembic/               # DB migrations
tests/                 # Automated tests
.github/workflows/     # CI configuration
docker-compose.yml     # PostgreSQL container
```

## 🚀 Setup & Run (Local)
### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Start PostgreSQL (Docker)
```bash
docker compose up -d
```
### 3. Run database migrations
```bash
alembic upgrade head
```
### 4. Start the API server
```bash
uvicorn app.main:app --reload
```
### 5. Open API docs
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🔌 Example Requests
### Create Product
```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "sku": "ABC-1",
    "name": "Teh Botol",
    "price": 5000,
    "stock": 10
  }'
```
### List Products
```bash
curl "http://127.0.0.1:8000/products?limit=50&offset=0"
```
### Create Order
```bash
curl -X POST "http://127.0.0.1:8000/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      { "product_id": 1, "qty": 2 }
    ]
  }'
```
## 💰 Money Handling
- Monetary values use Decimal, not float
- Prices are stored with fixed precision
- API responses serialize money safely (e.g. "7500.25")
## 📦 Stock Handling
- Stock is reduced automatically during order creation
- Order creation uses database transactions
- Order fails if stock is insufficient
- Designed to be PostgreSQL row-lock ready
## 🧪 Testing
- Isolated test database
- Covers:
  - Product creation & pagination
  - Order creation
  - Stock reduction
  - Insufficient stock handling
### Run tests locally:
```bash
pytest -q
```
## 🔁 CI (GitHub Actions)
- Tests run automatically on:
  - push
  - pull_request
- Ensures code quality before merge
## 🎯 Project Scope
This repository intentionally focuses on:
- Backend API
- Database correctness
- Transactions
- Testing & CI
## 📌 Notes
- .env is excluded from repository
- Use .env.example for local configuration
- SQLite is used only for testing
