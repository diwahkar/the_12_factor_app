from app.api.v1.routes import analyze_sentiment, SentimentRequest

def test_analyze_sentiment():

    positive = analyze_sentiment(SentimentRequest(text="I love this!"))
    negative = analyze_sentiment(SentimentRequest(text="I hate this!"))
    neutral = analyze_sentiment(SentimentRequest(text="This is a pen."))

    assert positive["sentiment"] == "positive"
    assert negative["sentiment"] == "negative"
    assert neutral["sentiment"] == "neutral"
