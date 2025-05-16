# github repo link
https://github.com/diwahkar/the_12_factor_app


# Sentiment Analysis Microservice

## What It Does
A FastAPI-based service that analyzes the sentiment of provided text.

## How to Run

### Local Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Using Docker
```bash
docker-compose up --build
```

## Configuration
Create a `.env` file:
```
API_KEY=your_secret_key_goes_here
```

## ✅ Run Tests
```bash
pytest
```

## 📂 API Endpoint
- **POST** `/api/v1/analyze`
  **Request:**
  ```json
  {
    "text": "I love using FastAPI!"
  }
  ```
  **Response:**
  ```json
  {
    "sentiment": "positive"
  }


