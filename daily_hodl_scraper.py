
#------------------------------------------------
# The Daily Hodl scraper (https://dailyhodl.com/)
#------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import eel

PATH = "C:\Program Files (x86)\chromedriver.exe"

def dailyHodl(query, amount):

#adding all necessary variables
    all_text = []
    titles = []
    srcs = []
    queries = query.split()
    counter = 0
    driver = webdriver.Chrome(PATH)

#for each query in queries
    for x in range(len(queries)):

        #searchs for query
        driver.get("https://dailyhodl.com/?s=")
        print(driver.title)
        search = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/form/input")
        search.send_keys(queries[x])
        search.send_keys(Keys.RETURN)

        try:

            #for i in amount of aticles to return
            for i in range(int(amount)):
            
                #waits until page is loaded and finds results contatiner
                container_el = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "jeg_posts.jeg_load_more_flag"))
                )

                #finds all search results in page
                results_el = container_el.find_elements(By.CLASS_NAME, "jeg_post.jeg_pl_md_2.format-standard")

                #cheks if each result is article
                if results_el[i].find_elements(By.CLASS_NAME, "jeg_thumb"):

                   #takes article's image url
                    img = results_el[i].find_element(By.TAG_NAME, "img")
                    srcs.append(img.get_attribute("src"))
            
                else:
                    continue

                #clicks on article's url
                a = results_el[i].find_element(By.TAG_NAME, "a")
                a.click()
    
                #waits until page is loaded
                body = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )                                                               
                
                #checks if article exist
                if body.find_elements(By.CLASS_NAME, "content-inner "):
                    
                    #finds article's text container
                    section = body.find_elements(By.CLASS_NAME, "content-inner ")[0]
                    
                    #saves all text from article's text container
                    all_text.append(section.text)
                    #saves title from article page
                    titles.append(driver.title) 

                else:
                    #if aticle does not exist adds some text
                    titles.append("Article not found")
                    all_text.append("Ooooops :(")
                
                counter += 1
                driver.back()
                driver.refresh()

        except Exception: 
            print("something went wrong(")

        finally:
            print("----------------------------------------------------")

    return titles, srcs, all_text, counter, queries