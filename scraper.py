from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


all_text = ""
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://selenium-python.readthedocs.io/")
print(driver.title)

search = driver.find_element(By.XPATH, "//*[@id='searchbox']/div/form/input[1]")
search.send_keys("click")
search.send_keys(Keys.RETURN)


ul = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "search"))
)

lis = ul.find_elements(By.TAG_NAME, "li")

try:
    for i in range(len(lis)):


        ul_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search"))
        )

        lis = ul_el.find_elements(By.TAG_NAME, "li")
    
        a = lis[i].find_element(By.TAG_NAME, "a")
        a.click()
    

        section = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "section"))
        )
        ps = section.find_elements(By.TAG_NAME, "p")

        for p in ps:
            all_text += "".join(p.text)

    
        driver.back()

finally:
    open('info.txt', 'w').close()
    file = open("info.txt", "a") #opens a file in the same folder with python script
    file.write(all_text) #writes all text to a file in the same folder with python script
    print(all_text)
    driver.close()








