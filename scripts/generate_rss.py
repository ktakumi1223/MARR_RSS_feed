import requests
from bs4 import BeautifulSoup
from feedgenerator import Rss201rev2Feed
import os

url = 'https://www.marr.jp/'  # MARR OnlineのURL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

feed = Rss201rev2Feed(
    title="MARR Online新着記事",
    link=url,
    description="MARR Onlineの新着記事RSS",
    language="ja"
)

# 以下はサイト構造により修正が必要な場合があります
articles = soup.select('div.topics-list a')[:10]

for article in articles:
    title = article.get_text(strip=True)
    link = article['href'] if article['href'].startswith('http') else f"https://www.marr.jp{article['href']}"
    feed.add_item(title=title, link=link, description=title)

rss_content = feed.writeString('utf-8')

os.makedirs('rss', exist_ok=True)
with open('rss/marr_online.xml', 'w', encoding='utf-8') as f:
    f.write(rss_content)
