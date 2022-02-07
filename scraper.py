from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


all_text = ""
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://currency.com/search")
print(driver.title)

search = driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div/label/input")
search.send_keys("etherium")
search.send_keys(Keys.RETURN)


container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
)

results = container.find_elements(By.CLASS_NAME, "global-search__item")

try:
    for i in range(1):

        container_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
        )

        results_el = container_el.find_elements(By.CLASS_NAME, "global-search__item")
    
        a = results_el[i].find_element(By.TAG_NAME, "a")
        a.click()
    

        section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inner-content-article"))
        )
        print(section.text)

        driver.back()
        driver.refresh()

finally:
    driver.close()