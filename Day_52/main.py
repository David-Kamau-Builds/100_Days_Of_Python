import os
import time
import random
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------------- CONFIG ---------------- #
load_dotenv()

URL = "https://instagram.com"

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

SIMILAR_ACCOUNT = "Instagram"  # Account whose followers to target

MAX_FOLLOWS_PER_RUN = 10          # Follow limit
SCROLL_CYCLES = 6                 # How many times to scroll followers modal
MIN_DELAY = 1.5
MAX_DELAY = 4.5


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Stealth-ish options (not bulletproof, but helps)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 12)


    def human_delay(self, a=MIN_DELAY, b=MAX_DELAY):
        time.sleep(random.uniform(a, b))

    def safe_click(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            self.human_delay()
            return True
        except TimeoutException:
            return False


    def login(self):
        self.driver.get(URL)
        self.human_delay(4, 6)

        # Cookies (sometimes shown, sometimes not)
        self.safe_click(By.XPATH, "//button[contains(text(),'Decline')]")

        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))

        username_input.send_keys(USERNAME)
        self.human_delay(1, 2)
        password_input.send_keys(PASSWORD)
        self.human_delay(1, 2)
        password_input.send_keys(Keys.ENTER)

        # Save login info popup
        self.safe_click(By.XPATH, "//button[contains(text(),'Not now')]")

        # Notifications popup
        self.safe_click(By.XPATH, "//button[contains(text(),'Not Now')]")


    def open_followers_modal(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        self.human_delay(4, 6)

        self.safe_click(By.XPATH, "//a[contains(@href,'/followers')]")

        # Wait for modal
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

    def scroll_followers(self):
        modal = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[contains(@style,'overflow')]"))
        )

        for _ in range(SCROLL_CYCLES):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            self.human_delay(2, 4)


    def follow(self):
        followed_count = 0

        buttons = self.driver.find_elements(
            By.XPATH, "//button[.//text()='Follow']"
        )

        for button in buttons:
            if followed_count >= MAX_FOLLOWS_PER_RUN:
                print("✅ Follow limit reached.")
                break

            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                self.human_delay(1, 2)
                button.click()
                followed_count += 1
                print(f"➕ Followed ({followed_count})")
                self.human_delay(3, 6)

            except ElementClickInterceptedException:
                try:
                    cancel_btn = self.driver.find_element(
                        By.XPATH, "//button[contains(text(),'Cancel')]"
                    )
                    cancel_btn.click()
                except NoSuchElementException:
                    pass

        print(f"🎯 Total followed this run: {followed_count}")


    def run(self):
        self.login()
        self.open_followers_modal()
        self.scroll_followers()
        self.follow()


if __name__ == "__main__":
    bot = InstaFollower()
    bot.run()