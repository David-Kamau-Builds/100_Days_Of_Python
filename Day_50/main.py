import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")

def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login_tinder(driver):
    driver.get("http://www.tinder.com")
    sleep(2)

    login_button = driver.find_element(By.XPATH, '//*[text()="Log in"]')
    login_button.click()
    sleep(2)

    fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
    sleep(2)

    base_window = driver.window_handles[0]
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)

    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
    email_field.send_keys(FB_EMAIL)
    password_field.send_keys(FB_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    driver.switch_to.window(base_window)
    sleep(5)

    # Handle location, notifications, cookies
    try:
        driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
    except NoSuchElementException:
        pass

def like_profiles(driver, max_likes=100):
    """Automatically like profiles up to max_likes."""
    for _ in range(max_likes):
        sleep(1)
        try:
            like_button = driver.find_element(By.XPATH,
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_button.click()
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:
                sleep(2)
        except NoSuchElementException:
            sleep(2)

def main():
    driver = init_driver()
    try:
        login_tinder(driver)
        like_profiles(driver, max_likes=100)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
