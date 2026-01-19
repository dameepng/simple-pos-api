# Simple POS API (FastAPI)

Backend POS sederhana (portfolio) dengan best practices:
- FastAPI
- SQLAlchemy
- Alembic migrations
- Layered architecture (routes → services → repositories)
- Swagger docs

## Features (today)
- Products
  - Create product
  - List products (pagination: limit & offset)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Alembic
- SQLite (dev)

## Project Structure
```text
app/
  api/
  core/
  db/
  models/
  repositories/
  schemas/
  services/
alembic/
```

## Setup & Run
```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Open
- http://127.0.0.1:8000/docs

## Example Requests
Create Product:
```bash
curl -X POST "http://127.0.0.1:8000/products" ^
  -H "Content-Type: application/json" ^
  -d "{\"sku\":\"ABC-1\",\"name\":\"Teh Botol\",\"price\":5000,\"stock\":10}"
```
List Product:
```bash
curl "http://127.0.0.1:8000/products?limit=50&offset=0"
```

## Stock
- Stock update during order creation uses transaction-safe logic
- Row-level locking is PostgreSQL-ready (SQLite fallback)
## Money Handling
- Monetary values are stored and calculated using Decimal
- API responses serialize money as string with 2 decimal places
## Quality
- Transaction-safe order processing
- Decimal-based money handling
- Automated tests with isolated DB
- CI with GitHub Actions

![CI](https://github.com/dameepng/simple-pos-api/actions/workflows/ci.yml/badge.svg)
