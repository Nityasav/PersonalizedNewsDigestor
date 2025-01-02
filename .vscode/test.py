import requests
import datetime
from transformers import pipeline
# References:
# NewsAPI docs: https://newsapi.org/docs
# Hugging Face Transformers pipelines: https://huggingface.co/docs/transformers/main_classes/pipelines
# Configuration
NEWS_API_KEY = "4281d8a24c9e482bb487f06684369577"
BASE_URL = "https://newsapi.org/v2/everything"
topics = ["finance", "crypto"]  # Example user selection
max_days_back = 14
# Date calculation
today = datetime.datetime.now()
from_date = (today - datetime.timedelta(days=max_days_back)).strftime("%Y-%m-%d")
to_date = today.strftime("%Y-%m-%d")
# Fetch articles
all_articles = []
for topic in topics:
    params = {
        "q": topic,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 50
    }
    response = requests.get(BASE_URL, params=params).json()
    if "articles" in response:
        for article in response["articles"]:
            # Check publish date
            published_at = datetime.datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
            if (today - published_at).days <= max_days_back:
                all_articles.append(article["content"] or "")
# Summarize collected content
text_to_summarize = " ".join(all_articles)
summarizer = pipeline("summarization")
summary = summarizer(text_to_summarize, max_length=150, min_length=30, do_sample=False)
print("Daily Digest Summary:")
print(summary[0]["summary_text"])