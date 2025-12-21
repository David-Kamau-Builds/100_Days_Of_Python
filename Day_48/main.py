import json
import os
import re
import time
import random
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv

load_dotenv()

URL = "https://jiji.co.ke/furniture?query=electric+height+adjustable"
JSON_FILE = "adjustable_desks.json"

ITEM_LIMIT = 100
MAX_RETRIES = 3
PARALLEL_TABS = 4
BATCH_DELAY = (3, 6)
PAGE_DELAY = (1.2, 2.2)

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")


def setup_driver(detach: bool = True) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", detach)
    return webdriver.Chrome(options=options)


def extract_price(price_text: str) -> int:
    return int(re.sub(r"[^\d]", "", price_text) or 0)


def human_sleep(delay_range: tuple[float, float]):
    """Sleep with random jitter to mimic human behavior"""
    time.sleep(random.uniform(*delay_range))


def scroll_until_items_loaded(driver, target_count=ITEM_LIMIT, pause=1.5, max_scrolls=40):
    last_count = 0
    for i in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        count = len(driver.find_elements(By.CLASS_NAME, "js-advert-list-item"))
        print(f"Scroll {i + 1}: {count} items loaded")
        if count >= target_count or count == last_count:
            break
        last_count = count


def collect_listing_data(driver) -> list[dict]:
    items = driver.find_elements(By.CLASS_NAME, "js-advert-list-item")
    listings = []
    for item in items[:ITEM_LIMIT]:
        try:
            name = item.find_element(By.CLASS_NAME, "qa-advert-title").text
            price = item.find_element(By.CLASS_NAME, "qa-advert-price").text
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            listings.append({
                "item_name": name,
                "price": price,
                "price_int": extract_price(price),
                "link": link,
            })
        except NoSuchElementException:
            continue
    print(f"Collected {len(listings)} listing links")
    return listings


def extract_seller_info(driver):
    vendor_name = ""

    try:
        try:
            vendor_name_elem = driver.find_element(
                By.XPATH,
                '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div[2]/a[1]/div[2]/div[1]'
            )
            vendor_name = vendor_name_elem.text.strip()
        except NoSuchElementException:
            vendor_name = ""

    except Exception as e:
        print(f"Error extracting seller info: {e}")

    return vendor_name


def scrape_item_page(driver, item: dict) -> dict:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            driver.get(item["link"])
            human_sleep(PAGE_DELAY)

            item["description"] = driver.find_element(
                By.CLASS_NAME, "qa-description-text"
            ).text.strip()

            vendor_name = extract_seller_info(driver)
            item["vendor_name"] = vendor_name

            return item

        except (NoSuchElementException, TimeoutException):
            print(f"Retry {attempt}/{MAX_RETRIES} failed for {item['item_name']}")
            human_sleep((1.5, 3))

    item["description"] = ""
    item["vendor_name"] = ""
    return item


def scrape_in_parallel(driver, listings: list[dict]) -> list[dict]:
    results = []
    main_tab = driver.current_window_handle

    for i in range(0, len(listings), PARALLEL_TABS):
        batch = listings[i:i + PARALLEL_TABS]
        print(f"\nProcessing batch {i // PARALLEL_TABS + 1}")

        for item in batch:
            driver.execute_script(f"window.open('{item['link']}');")
            human_sleep((0.3, 0.6))

        tabs = driver.window_handles
        for tab, item in zip(tabs[1:], batch):
            driver.switch_to.window(tab)
            print(f"Scraping: {item['item_name']}")
            enriched = scrape_item_page(driver, item)
            results.append(enriched)
            driver.close()

        driver.switch_to.window(main_tab)
        human_sleep(BATCH_DELAY)

    return results


def save_to_json(data: list[dict]):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\nSaved {len(data)} items to {JSON_FILE}")


def send_email_alert(items):
    sorted_items = sorted(items, key=lambda x: x["price_int"])
    cheapest = sorted_items[:8]
    expensive = sorted_items[-8:][::-1]  # descending

    msg = EmailMessage()
    msg["Subject"] = "Top Adjustable Desks on Jiji (Cheapest & Most Expensive)"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    text_content = "Top 8 Cheapest Desks:\n"
    for desk in cheapest:
        text_content += f"Name: {desk['item_name']}\nPrice: {desk['price']}\nLink: {desk['link']}\n{'-'*40}\n"

    text_content += "\nTop 8 Most Expensive Desks:\n"
    for desk in expensive:
        text_content += f"Name: {desk['item_name']}\nPrice: {desk['price']}\nLink: {desk['link']}\n{'-'*40}\n"

    html_content = "<h2>Top 8 Cheapest Desks</h2><ul>"
    for desk in cheapest:
        html_content += f"<li><strong>{desk['item_name']}</strong><br>Price: {desk['price']}<br><a href='{desk['link']}'>View Deal</a></li><br>"
    html_content += "</ul>"

    html_content += "<h2>Top 8 Most Expensive Desks</h2><ul>"
    for desk in expensive:
        html_content += f"<li><strong>{desk['item_name']}</strong><br>Price: {desk['price']}<br><a href='{desk['link']}'>View Deal</a></li><br>"
    html_content += "</ul>"

    msg.set_content(text_content)
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    driver = setup_driver()
    driver.get(URL)

    scroll_until_items_loaded(driver)
    listings = collect_listing_data(driver)
    desks = scrape_in_parallel(driver, listings)

    save_to_json(desks)

    send_email_alert(desks)

    driver.quit()


if __name__ == "__main__":
    main()
