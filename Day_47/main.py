import os
import re
import json
import sys
import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage
from dotenv import load_dotenv
from urllib.parse import urljoin

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

try:
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
except (TypeError, ValueError):
    print("Error: SMTP_PORT must be a valid integer in .env")
    sys.exit(1)

if not all([SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL]):
    print("Error: Missing required environment variables.")
    sys.exit(1)

JSON_FILE = "adjustable_desks.json"
SEARCH_URL = "https://jiji.co.ke/furniture"
LINKS_BASE_URL = "https://jiji.co.ke"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def extract_price(price_str):
    if not price_str:
        return None
    digits = re.sub(r"[^\d]", "", price_str)
    return int(digits) if digits else None

def scrape_jiji_desks():
    parameters = {"query": "electric+height+adjustable"}
    
    try:
        response = requests.get(SEARCH_URL, params=parameters, headers=HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all("div", class_="b-list-advert__gallery__item js-advert-list-item")

    adjustable_desks = []

    for card in cards:
        name_tag = card.select_one(".b-advert-title-inner")
        price_tag = card.select_one(".b-list-advert__price-base")
        desc_tag = card.select_one(".b-list-advert-base__description-text")
        a_tag = card.find("a", href=True)

        name = name_tag.get_text(strip=True) if name_tag else "N/A"
        price = price_tag.get_text(strip=True) if price_tag else None
        description = desc_tag.get_text(strip=True) if desc_tag else ""
        link = urljoin(LINKS_BASE_URL, a_tag["href"]) if a_tag else None

        price_int = extract_price(price)

        if price_int: 
            adjustable_desks.append({
                "name": name,
                "price": price,
                "price_int": price_int,
                "description": description,
                "link": link
            })
    
    return adjustable_desks

def send_email_alert(items):
    msg = EmailMessage()
    msg["Subject"] = "Top 5 Cheapest Adjustable Desks on Jiji"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    text_content = ""
    html_content = "<h2>Top 5 Cheapest Adjustable Desks</h2><ul>"

    for desk in items:
        text_content += f"Name: {desk['name']}\nPrice: {desk['price']}\nLink: {desk['link']}\n{'-'*40}\n"
        html_content += f"<li><strong>{desk['name']}</strong><br>Price: {desk['price']}<br><a href='{desk['link']}'>View Deal</a></li><br>"
    
    html_content += "</ul>"

    msg.set_content(text_content)
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully ✅")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    print("🔎 Scraping Jiji for desks...")
    desks = scrape_jiji_desks()

    if not desks:
        print("No desks found matching criteria.")
        return

    adjustable_desks_sorted = sorted(desks, key=lambda x: x["price_int"])[:5]

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(adjustable_desks_sorted, f, ensure_ascii=False, indent=4)
    print(f"✅ Saved top 5 desks to {JSON_FILE}")

    send_email_alert(adjustable_desks_sorted)

if __name__ == "__main__":
    main()
