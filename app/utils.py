import json

FILENAME = 'article.json'

def read_articles():
    
    try:
        with open (FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_article(articles):
    with open(FILENAME, 'w') as f:
        json.dump(articles, f, indent=2)