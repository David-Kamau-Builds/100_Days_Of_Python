from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

LISTINGS_PAGE_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd109dXYjvbgw1TpR54S6x5eRpBVdie6B1sZHVCBScnc0-HKA/viewform?usp=dialog"

def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def get_listings(driver):
    wait = WebDriverWait(driver, 10)
    listings = []

    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div[class^="StyledCard"]')
        )
    )

    for card in cards:
        listings.append({
            "address": card.find_element(
                By.CSS_SELECTOR, 'address[data-test="property-card-addr"]'
            ).text,
            "price": card.find_element(
                By.CSS_SELECTOR, 'span[data-test="property-card-price"]'
            ).text,
            "link": card.find_element(
                By.CSS_SELECTOR, 'a[data-test="property-card-link"]'
            ).get_attribute("href")
        })

    return listings

def submit_listing(driver, listing):
    wait = WebDriverWait(driver, 10)

    # Get ONLY visible & enabled text inputs
    inputs = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'input[type="text"]')
        )
    )

    visible_inputs = [i for i in inputs if i.is_displayed() and i.is_enabled()]

    if len(visible_inputs) < 3:
        raise Exception("Not enough visible input fields found")

    # Scroll & fill
    driver.execute_script("arguments[0].scrollIntoView(true);", visible_inputs[0])
    visible_inputs[0].send_keys(listing["address"])

    visible_inputs[1].send_keys(listing["price"])
    visible_inputs[2].send_keys(listing["link"])

    # Submit button
    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div[role="button"][aria-label="Submit"]')
        )
    )
    submit_btn.click()

    # Submit another response
    wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Submit another response")
        )
    ).click()


def main():
    driver = init_driver()

    driver.get(LISTINGS_PAGE_URL)
    listings = get_listings(driver)

    driver.get(GOOGLE_FORMS_URL)

    for listing in listings:
        submit_listing(driver, listing)
        time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    main()
