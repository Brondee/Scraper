from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import eel
from coindesk_scraper import coindesk
from daily_hold_scraper import dailyHold

#eel.init("web")

PATH = "C:\Program Files (x86)\chromedriver.exe"

#@eel.expose
def cryptocurrency(query, amount):

    all_text = []
    titles = []
    srcs = []
    queries = query.split()
    counter = 0
    driver = webdriver.Chrome(PATH)

    for x in range(len(queries)):

        driver.get("https://currency.com/search")
        print(driver.title)
        search = driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div/label/input")
        search.send_keys(queries[x])
        search.send_keys(Keys.RETURN)




        try:
            for i in range(int(amount)):
            
                container_el = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
                )

                results_el = container_el.find_elements(By.CLASS_NAME, "global-search__item")

                if results_el[i].find_elements(By.CLASS_NAME, "global-search__img"):

                    img = results_el[i].find_element(By.TAG_NAME, "img")
                    srcs.append(img.get_attribute("src"))
            
                else:
                    continue

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

        finally:
            #open('info.txt', 'w').close()
            #file = open("info.txt", "a") #opens a file in the same folder with python script
            #file.write(all_text) #writes all text to a file in the same folder with python script
            #print(all_text)
            #print(srcs)
            #print(counter)
            print("----------------------------------------------------")
    
    #daily_hold_info = dailyHold(query, amount)

    #print(daily_hold_info)

    #for t in range(daily_hold_info[3]):

        #titles.append(daily_hold_info[0][t])
        #srcs.append(daily_hold_info[1][t])
        #all_text.append(daily_hold_info[2][t])
        #counter += daily_hold_info[3]

    #print(titles)
    return titles, srcs, all_text, counter, queries

#eel.start("index.html", size = (1500, 900))