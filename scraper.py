from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://selenium-python.readthedocs.io/api.html")
print(driver.title)

search = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/form/input[1]")
search.send_keys("click")
search.send_keys(Keys.RETURN)

try:
    ul = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search"))
    )
    a = ul.find_element(By.TAG_NAME, "a")
    a.click()

    section = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "webdriver-api"))
    )
    ps = section.find_elements(By.TAG_NAME, "p")

    for p in ps:
        print(p.text)

except Exception:
    driver.close()







