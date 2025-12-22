from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep

URL = "https://ozh.github.io/cookieclicker/"
RUN_TIME = 5 * 60
DASHBOARD_INTERVAL = 1
LANGUAGE_ID = "langSelect-EN"


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)


def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def select_language(driver):
    try:
        wait_for(driver, By.ID, LANGUAGE_ID).click()
    except:
        pass

def start_fast_clicking(driver):
    driver.execute_script()


def click_golden_cookie(driver):
    driver.execute_script()


def buy_best_roi(driver):
    driver.execute_script()


def get_stats(driver):
    return driver.execute_script()



def main():
    driver = setup_driver()
    driver.get(URL)

    select_language(driver)
    wait_for(driver, By.ID, "bigCookie")

    start_fast_clicking(driver)

    start = time()
    next_dashboard = time()

    while time() - start < RUN_TIME:
        click_golden_cookie(driver)
        buy_best_roi(driver)

        if time() >= next_dashboard:
            stats = get_stats(driver)
            print(
                f"🍪 Cookies: {int(stats['cookies']):,} | "
                f"⚙ CPS: {stats['cps']:.1f} | "
                f"🏆 Total Earned: {int(stats['total']):,}"
            )
            next_dashboard = time() + DASHBOARD_INTERVAL

        sleep(0.1)

    print("\n=== FINAL STATS ===")
    stats = get_stats(driver)
    print(f"Cookies: {int(stats['cookies']):,}")
    print(f"CPS: {stats['cps']:.1f}")
    print(f"Total Earned: {int(stats['total']):,}")


if __name__ == "__main__":
    main()
