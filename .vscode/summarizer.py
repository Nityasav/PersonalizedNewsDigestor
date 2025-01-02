from transformers import pipeline

summarizer_pipeline = pipeline("summarization")
def summarize_text(text):
    summary = summarizer_pipeline(text, max_length=150, min_length=100, do_sample=False)
    return summary[0]["summary_text"]