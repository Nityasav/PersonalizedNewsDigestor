def generate_report(summarized_articles):
    lines = []
    lines.append("Latest News Digest:\n")
    for article in summarized_articles:
        lines.append(f"Topic: {article['topic']}")
        lines.append(f"Title: {article['title']}")
        lines.append(f"Summary: {article['summary']}")
        lines.append(f"URL: {article['url']}")
        lines.append("")
    return "\n".join(lines)