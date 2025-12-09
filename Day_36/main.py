from datetime import datetime, timedelta, timezone
import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
STOCKS_FUNCTION = "TIME_SERIES_DAILY"
NEWS_FUNCTION = "NEWS_SENTIMENT"
TICKERS = STOCK_NAME
SORT = "LATEST"
ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"

# Twilio config
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_FROM_NUMBER = "whatsapp:+YOUR_TWILIO_NUMBER"  # your Twilio number
TO_NUMBER = "whatsapp:+YOUR_PHONE_NUMBER"            # your phone number

# -----------------------------
# Helper functions
# -----------------------------
def percent_difference(latest, previous):
    difference = latest - previous
    percent = round((difference / previous) * 100, 2)
    return percent

def format_time_published(time_str):
    dt_utc = datetime.strptime(time_str, "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc)
    dt_local = dt_utc.astimezone()  # system local time
    formatted_local = dt_local.strftime("%Y-%m-%d, %H:%M")
    formatted_utc = dt_utc.strftime("%Y-%m-%d, %H:%M UTC")
    return formatted_local, formatted_utc



stock_params = {
    "function": STOCKS_FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()

if "Time Series (Daily)" not in stock_data:
    print("API limit reached or invalid response:")
    print(stock_data)
    exit()

time_series = stock_data["Time Series (Daily)"]
dates = sorted(time_series.keys(), reverse=True)
latest = dates[0]
previous = dates[1]

latest_close = float(time_series[latest]["4. close"])
previous_close = float(time_series[previous]["4. close"])
pct_diff = percent_difference(latest_close, previous_close)

print(f"Latest trading day: {latest}. Close: {latest_close}")
print(f"Previous trading day: {previous}. Close: {previous_close}")
print(f"Percent difference: {pct_diff:+.2f}%")


news_params = {
    "function": NEWS_FUNCTION,
    "tickers": TICKERS,
    "sort": SORT,
    "apikey": API_KEY
}

response = requests.get(ENDPOINT, params=news_params)
response.raise_for_status()
news_data = response.json()

if "feed" not in news_data:
    print("No news available:")
    print(news_data)
    exit()


top_3_news = news_data["feed"][:5]

extracted_articles = []
for article in top_3_news:
    _, time_utc = format_time_published(article["time_published"])  # only need UTC time
    extracted_articles.append({
        "title": article["title"],
        "summary": article["summary"],
        "url": article["url"],
        "source": article["source"],
        "time_utc": time_utc
    })

# Print formatted articles
for art in extracted_articles:
    print(f"Title: {art['title']}")
    print(f"Summary: {art['summary']}")
    print(f"URL: {art['url']}")
    print(f"Source: {art['source']}")
    print(f"Published (UTC): {art['time_utc']}")
    print("-" * 50)



if abs(pct_diff) > -5:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for art in extracted_articles:
        message = (
            f"{STOCK_NAME}: {pct_diff:+.2f}%\n"
            f"HEADLINE: {art['title']}\n\n"
            f"Brief: {art['summary']}\n\n"
            f"Source: {art['source']}\n\n"
            f"Published: ({art['time_utc']})\n\n"
            f"URL: {art['url']}"
        )
        client.messages.create(
            body=message,
            from_=TWILIO_FROM_NUMBER,
            to=TO_NUMBER
        )
        print("Message sent for article:", art["title"])
