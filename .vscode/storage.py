import json
import os
STORAGE_FILE = "articles.json"
def load_articles():
    if not os.path.exists(STORAGE_FILE):
        return []
def save_articles(articles):
    with open(STORAGE_FILE, "w") as f:
        json.dump(articles, f, indent=2)