import feedparser

url = "https://example.com/rss"
feed = feedparser.parse(url)

print(f"Загружено {len(feed.entries)} новостей")
print("RSS парсер №2 запущен")
