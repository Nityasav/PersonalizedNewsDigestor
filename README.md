Description
This project fetches news articles based on user-selected topics, processes them, and provides summaries using advanced natural language processing techniques.
Features

Topic-based news retrieval
Article information extraction (title, description, content, URL, publish date)
Automatic article summarization using Hugging Face pipelines
User-friendly interface for browsing and filtering articles

Installation
1. Clone the repository
2. Install required dependencies: pip install -r requirements.txt
3. Set up your NewsAPI key in the configuration file
   
Usage
1. Run the main script: python news_aggregator.py
Select your desired topics
2. Browse through the fetched articles and their summaries
Configuration
3. API key: Add your NewsAPI key to config.py
4. Customize topic list in topics.py
5. Adjust summarization parameters in summarizer.py
   
Dependencies
NewsAPI
Hugging Face Transformers
[Other relevant libraries]

Acknowledgments
NewsAPI for providing access to news articles
Hugging Face for their excellent NLP tools and models
