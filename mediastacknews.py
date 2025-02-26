import requests

# ✅ Mediastack API Key
API_KEY = "32e37a90c0ea80197b1da2d35d795abd"

# ✅ Mediastack API Endpoint (Fetching English news for Maharashtra)
URL = f"http://api.mediastack.com/v1/news?access_key={API_KEY}&countries=in&languages=en&keywords=Maharashtra"

# ✅ Fetch News
def get_maharashtra_news():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to fetch news:", response.json())
        return "⚠️ *माहिती आणता आली नाही!*"

    data = response.json()
    articles = data.get("data", [])

    if not articles:
        return "❌ *आज महाराष्ट्र संबंधित कोणतीही बातमी उपलब्ध नाही.*"

    news_list = []
    for article in articles[:5]:  # Fetch latest 5 news
        title = article.get("title", "No Title")
        url = article.get("url", "#")
        news_list.append(f"📰 *{title}*\n🔗 [वाचा अधिक]({url})\n")

    return "\n".join(news_list)

# ✅ Run
news_message = get_maharashtra_news()
print(news_message)
