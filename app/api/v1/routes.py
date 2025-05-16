from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal

router = APIRouter()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral']


@router.get('/')
def hello_func():
    return 'test hello'



@router.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    text = request.text.lower()
    if "good" in text or "love" in text:
        return {"sentiment": "positive"}
    elif "bad" in text or "hate" in text:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}
