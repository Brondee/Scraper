from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import eel

PATH = "C:\Program Files (x86)\chromedriver.exe"

def coindesk(query, amount):

    coin_all_text = []
    coin_titles = []
    coin_srcs = []
    queries = query.split()
    counter = 0
    driver = webdriver.Chrome(PATH)

    for x in range(len(queries)):

        driver.get("https://www.coindesk.com/search?s=")
        print(driver.title)
        search = driver.find_element(By.CLASS_NAME, "text-field__StyledInput-sc-46zp4l-3.erYDVg")
        search.send_keys(queries[x])
        search.send_keys(Keys.RETURN)


        container = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "searchstyles__ResultsData-ci5zlg-2.fTmqCA"))
        )

        results = container.find_elements(By.CLASS_NAME, "searchstyles__ItemRow-ci5zlg-4.cjNxdI")

        try:
            for i in range(int(amount)):
            
                container_el = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "searchstyles__ResultsData-ci5zlg-2.fTmqCA"))
                )

                results_el = container_el.find_elements(By.CLASS_NAME, "searchstyles__ItemRow-ci5zlg-4.cjNxdI")

                if results_el[i].find_elements(By.CLASS_NAME, "searchstyles__ImageContainer-ci5zlg-7.EeZIR"):

                    img = results_el[i].find_element(By.TAG_NAME, "img")
                    coin_srcs.append(img.get_attribute("src"))
            
                else:
                    continue

                a = results_el[i].find_element(By.TAG_NAME, "a")
                a.click()
    
        
                section = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "main"))
                )                                                               

                coin_all_text.append(section.text)
                coin_titles.append(driver.title) 

                counter += 1
                driver.back()
                driver.refresh()

        finally:
            #open('info.txt', 'w').close()
            #file = open("info.txt", "a") #opens a file in the same folder with python script
            #file.write(all_text) #writes all text to a file in the same folder with python script
            print(coin_all_text)
            print(coin_srcs)
            print(counter)
            print("----------------------------------------------------")

    return coin_titles, coin_srcs, coin_all_text, counter, queries

#print(coindesk("bitcoin litecoin", "2"))