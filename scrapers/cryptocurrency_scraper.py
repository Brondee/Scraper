
#---------------------------------------------------
# Cryptocurrency.com scraper (https://currency.com/)
#---------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"

def cryptocurrency(query, amount):

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
        driver.get("https://currency.com/search")
        search = driver.find_element(By.XPATH, "/html/body/div[1]/form[1]/div/label/input")
        search.send_keys(queries[x])
        search.send_keys(Keys.RETURN)

        try:

            #for i in amount of aticles to return
            for i in range(int(amount)):
                
                #waits until page is loaded and finds results contatiner
                container_el = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "global-search__list"))
                )
                
                #finds all search results in page
                results_el = container_el.find_elements(By.CLASS_NAME, "global-search__item")
                
                #cheks if each result is article
                if results_el[i].find_elements(By.CLASS_NAME, "global-search__img"):
                    
                    #takes article's image url
                    img = results_el[i].find_element(By.TAG_NAME, "img")
                    srcs.append(img.get_attribute("src"))

                else:
                    continue
                
                #clicks on article's url
                a = results_el[i].find_element(By.TAG_NAME, "a")
                a.click()
    
                #waits until page is loaded and finds article's text container
                section = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "inner-content-article"))
                )

                #saves all text from article's text container
                all_text.append(section.text)
                #saves title from article page
                titles.append(driver.title) 

                counter += 1
                driver.back()
                driver.refresh()

        except Exception: 
            print("something went wrong(")
            
        finally:
            print(counter)
    
    #returns all information
    return titles, srcs, all_text, counter, queries