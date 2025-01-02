from datetime import datetime, timedelta
from config import NEWS_API_KEY, NEWS_API_ENDPOINT, DAYS_LIMIT
import requests
def fetch_articles(topics):
    cutoff_date = (datetime.now() - timedelta(days=DAYS_LIMIT)).isoformat("T") + "Z"
    all_articles = []
    for topic in topics:
        params = {
            "q": topic,
            "from": cutoff_date,
            "sortBy": "publishedAt",
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "pageSize": 50
        }
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        data = response.json()
        if data.get("articles"):
            for article in data["articles"]:
                all_articles.append({
                    "title": article["title"],
                    "description": article.get("description"),
                    "content": article.get("content"),
                    "url": article["url"],
                    "publishedAt": article["publishedAt"],
                    "topic": topic
                })
    return all_articles