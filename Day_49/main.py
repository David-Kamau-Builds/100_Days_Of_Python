import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://appbrewery.github.io/gym/"

STUDENT_USERNAME = "TestUser42"
STUDENT_EMAIL = "testuser42@example.com"
STUDENT_PASSWORD = "Passw0rd!2025"


LOGIN_BUTTON = "Navigation_button__uyKX2"
TOGGLE_BUTTON = "Login_toggleButton___tVY8"
SUBMIT_BUTTON = "Login_submitButton__tJFna"
ERROR_MESSAGE = "Login_errorMessage__5r698"


def setup_driver(detach=True):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", detach)
    return webdriver.Chrome(options=options)


def retry(func, retries=7, description=None, delay=1):
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            print(f"[Retry {attempt}/{retries}] {description or func.__name__} failed → {e}")
            if attempt == retries:
                raise
            time.sleep(delay)


def element_exists(driver, by, value, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False


def login(driver):
    # Open login modal
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, LOGIN_BUTTON))
    ).click()

    # Switch to register/login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, TOGGLE_BUTTON))
    ).click()

    # Register
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys(STUDENT_USERNAME)

    driver.find_element(By.NAME, "email").send_keys(STUDENT_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(STUDENT_PASSWORD)
    driver.find_element(By.CLASS_NAME, SUBMIT_BUTTON).click()

    # If user exists, switch to login
    if element_exists(driver, By.CLASS_NAME, ERROR_MESSAGE):
        driver.find_element(By.CLASS_NAME, TOGGLE_BUTTON).click()

        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email.clear()
        email.send_keys(STUDENT_EMAIL)

        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys(STUDENT_PASSWORD)

        driver.find_element(By.CLASS_NAME, SUBMIT_BUTTON).click()

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'My Bookings')]")
        )
    )


def list_available_classes(driver, class_type=None):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-class-type]"))
    )
    cards = driver.find_elements(By.CSS_SELECTOR, "div[data-class-type]")
    results = []

    for card in cards:
        c_type = card.get_attribute("data-class-type")
        if class_type and c_type != class_type:
            continue

        # Extract info
        try:
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text.strip()
        except:
            time_text = "Unknown"
        try:
            instructor = card.find_element(By.CSS_SELECTOR, "p[id^='class-instructor-']").text.strip()
        except:
            instructor = "Unknown"
        try:
            duration = card.find_element(By.CSS_SELECTOR, "p[id^='class-duration-']").text.strip()
        except:
            duration = "Unknown"

        button = card.find_element(By.TAG_NAME, "button")
        btn_text = button.text.strip().lower()

        if btn_text in ("booked", "cancel booking"):
            status = "Booked"
        elif btn_text in ("waitlisted", "leave waitlist"):
            status = "Waitlisted"
        else:
            status = "Available"

        results.append({
            "card_element": card,
            "type": c_type,
            "time": time_text,
            "instructor": instructor,
            "duration": duration,
            "status": status,
        })

    return results


def book_selected_classes(driver, classes_to_book):
    booked = 0
    waitlisted = 0
    already_done = 0

    for c in classes_to_book:
        button = c["card_element"].find_element(By.TAG_NAME, "button")
        btn_text = button.text.strip().lower()
        if btn_text in ("booked", "cancel booking", "waitlisted", "leave waitlist"):
            already_done += 1
            continue
        elif btn_text == "book class":
            button.click()
            WebDriverWait(driver, 10).until(lambda d: button.text.lower() in ("booked", "cancel booking"))
            booked += 1
        elif btn_text == "join waitlist":
            button.click()
            WebDriverWait(driver, 10).until(lambda d: button.text.lower() in ("waitlisted", "leave waitlist"))
            waitlisted += 1

    print("\n--- BOOKING SUMMARY ---")
    print(f"Classes booked: {booked}")
    print(f"Waitlists joined: {waitlisted}")
    print(f"Already booked/waitlisted: {already_done}")


def main():
    driver = setup_driver()
    driver.get(URL)

    retry(lambda: login(driver), description="Login")

    # List all available classes
    # to specify a class type, pass it as class_type argument e.g. "class_type='yoga'", class_type="spin"
    available_classes = retry(lambda: list_available_classes(driver, class_type=""),
                              description="List available classes")

    if not available_classes:
        print("No classes found.")
        return

    # Show numbered list
    print("\n--- AVAILABLE CLASSES ---")
    for i, c in enumerate(available_classes, start=1):
        print(f"{i}. {c['type']} | {c['time']} | {c['instructor']} | {c['duration']} | {c['status']}")

    # Ask user which classes to book
    choices = input("Enter the numbers of classes you want to book (comma-separated): ")
    try:
        selected_indices = [int(x.strip()) - 1 for x in choices.split(",") if x.strip().isdigit()]
    except:
        print("Invalid input.")
        return

    classes_to_book = [available_classes[i] for i in selected_indices if 0 <= i < len(available_classes)]
    if not classes_to_book:
        print("No valid classes selected.")
        return

    retry(lambda: book_selected_classes(driver, classes_to_book), description="Book selected classes")


if __name__ == "__main__":
    main()
