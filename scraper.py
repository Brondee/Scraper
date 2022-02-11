from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import eel

eel.init("web")

PATH = "C:\Program Files (x86)\chromedriver.exe"

@eel.expose
def scraper(query, amount):

    all_text = []
    titles = []
    srcs = []
    counter = 0
    driver = webdriver.Chrome(PATH)
    driver.get("https://currency.com/search")
    print(driver.title)

    search = driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div/label/input")
    search.send_keys(query)
    search.send_keys(Keys.RETURN)


    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
    )

    results = container.find_elements(By.CLASS_NAME, "global-search__item")

    try:
        for i in range(int(amount)):
            
            container_el = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
            )

            results_el = container_el.find_elements(By.CLASS_NAME, "global-search__item")

            img = results_el[i].find_element(By.TAG_NAME, "img")
            srcs.append(img.get_attribute("src")) 

            a = results_el[i].find_element(By.TAG_NAME, "a")
            a.click()
    
        
            section = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inner-content-article"))
            )
            all_text.append(section.text)
            titles.append(driver.title) 

            counter += 1
            driver.back()
            driver.refresh()

        return titles, srcs, all_text, counter

    finally:
        #open('info.txt', 'w').close()
        #file = open("info.txt", "a") #opens a file in the same folder with python script
        #file.write(all_text) #writes all text to a file in the same folder with python script
        print(all_text)
        print(srcs)
        print(counter)
        print("----------------------------------------------------")

eel.start("index.html", size = (1500, 900))