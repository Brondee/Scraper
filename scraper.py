from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


all_text = ""
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://cointelegraph.com/search?query=btc")
print(driver.title)

search = driver.find_element(By.ID, "search")
search.send_keys("eth")
search.send_keys(Keys.RETURN)


container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "post_container"))
)

results = container.find_elements(By.CLASS_NAME, "row.result")

try:
    for i in range(1):


        container_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post_container"))
        )

        results_el = container_el.find_elements(By.CLASS_NAME, "row.result")
    
        a_container = results_el[i].find_element(By.CLASS_NAME, "header")
        a = a_container.find_element(By.TAG_NAME, "a")
        a.click()
    

        section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post__article"))
        )
        print(section.text)

        driver.back()

finally:
    driver.close()