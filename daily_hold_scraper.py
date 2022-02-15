from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import eel

PATH = "C:\Program Files (x86)\chromedriver.exe"

def dailyHold(query, amount):

    coin_all_text = []
    coin_titles = []
    coin_srcs = []
    queries = query.split()
    counter = 0
    driver = webdriver.Chrome(PATH)

    for x in range(len(queries)):

        driver.get("https://dailyhodl.com/?s=")
        print(driver.title)
        search = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/form/input")
        search.send_keys(queries[x])
        search.send_keys(Keys.RETURN)


        

        try:
            for i in range(int(amount)):
            
                container_el = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "jeg_posts.jeg_load_more_flag"))
                )

                results_el = container_el.find_elements(By.CLASS_NAME, "jeg_post.jeg_pl_md_2.format-standard")

                if results_el[i].find_elements(By.CLASS_NAME, "jeg_thumb"):

                    img = results_el[i].find_element(By.TAG_NAME, "img")
                    coin_srcs.append(img.get_attribute("src"))
            
                else:
                    continue

                a = results_el[i].find_element(By.TAG_NAME, "a")
                a.click()
    
        
                body = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )                                                               

                if body.find_elements(By.CLASS_NAME, "content-inner "):
                    
                    section = body.find_elements(By.CLASS_NAME, "content-inner ")[0]

                    coin_all_text.append(section.text)
                    coin_titles.append(driver.title) 

                else:
                    coin_all_text.append("Ooooops :(")
                    coin_titles.append("Article not found") 
                
                counter += 1
                driver.back()
                driver.refresh()

        finally:
            #open('info.txt', 'w').close()
            #file = open("info.txt", "a") #opens a file in the same folder with python script
            #file.write(all_text) #writes all text to a file in the same folder with python script
            #print(coin_all_text)
            #print(coin_srcs)
            #print(counter)
            print("----------------------------------------------------")

    return coin_titles, coin_srcs, coin_all_text, counter, queries

#print(dailyHold("bitcoin litecoin", "2"))