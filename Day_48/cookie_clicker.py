from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

URL = "https://ozh.github.io/cookieclicker/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get(URL)

try:
    wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
except:
    pass


sleep(3)

# Inject a JS loop that clicks the cookie and buys upgrades/products
driver.execute_script("""
if (!window.fastClicker) {
    window.fastClicker = setInterval(() => {
        // Click the big cookie
        Game.ClickCookie();

        // Buy available upgrades first
        Game.UpgradesInStore.forEach(u => u.buy());

        // Buy most expensive affordable product
        Game.ObjectsById.slice().reverse().forEach(o => {
            if (Game.cookies >= o.price) o.buy();
        });
    }, 1);  // runs as fast as the JS engine allows (~1000× faster than Python clicks)
}
""")

print("Max-speed clicker activated! Watch the cookies explode...")
