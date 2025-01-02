Description
This project fetches news articles based on user-selected topics, processes them, and provides summaries using advanced natural language processing techniques.
Features
Topic-based news retrieval
Article information extraction (title, description, content, URL, publish date)
Automatic article summarization using Hugging Face pipelines
User-friendly interface for browsing and filtering articles
Installation
Clone the repository
Install required dependencies: pip install -r requirements.txt
Set up your NewsAPI key in the configuration file
Usage
Run the main script: python news_aggregator.py
Select your desired topics
Browse through the fetched articles and their summaries
Configuration
API key: Add your NewsAPI key to config.py
Customize topic list in topics.py
Adjust summarization parameters in summarizer.py
Dependencies
NewsAPI
Hugging Face Transformers
[Other relevant libraries]
Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments
NewsAPI for providing access to news articles
Hugging Face for their excellent NLP tools and models
