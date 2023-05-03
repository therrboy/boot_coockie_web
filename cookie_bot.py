from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:/Users/Rodrigo/PycharmProjects/Development/chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)
CLICKABLE = "rgba(238, 238, 238, 1)"  # color cuando el cuadro es clickeable


def click_cookie(seconds):
    cookie = driver.find_element(By.ID, "cookie")
    t_end = time.time() + seconds
    while time.time() < t_end:
        cookie.click()
        time.sleep(0.001)

def buy_power_up():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")  # Lista de todos los divs del sector
    for item in reversed(store):
        if item.value_of_css_property("background-color") == CLICKABLE:
            item.click()
            break

end = time.time() + 10
print(end)


while time.time() < end:
    click_cookie(5)
    buy_power_up()
    print(time.time())
