from config import PREFERRED_TOPICS, MAX_ARTICLES
from fetcher import fetch_articles
from summarizer import summarize_text
from storage import load_articles, save_articles
from report import generate_report
def run_digest():
    existing_articles = load_articles()
    existing_urls = {a["url"] for a in existing_articles}
    new_articles = fetch_articles(PREFERRED_TOPICS)
    filtered_articles = [a for a in new_articles if a["url"] not in existing_urls]
    summarized_articles = []
    for article in filtered_articles[:MAX_ARTICLES]:
        content_to_summarize = article["description"] or article["content"] or article["title"]
        if content_to_summarize:
            summary = summarize_text(content_to_summarize)
            article["summary"] = summary
            summarized_articles.append(article)
    updated_articles = existing_articles + summarized_articles
    save_articles(updated_articles)
    report = generate_report(summarized_articles)
    print(report)

if __name__ == "__main__":
    run_digest()