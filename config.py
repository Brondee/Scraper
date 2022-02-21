import eel
import sys

sys.path.append("/phyton_scraper/scrapers")

#importing all scrapers
from scrapers import daily_hodl_scraper
from scrapers import cryptocurrency_scraper

#asserting functions to variables
dailyHodl = daily_hodl_scraper.dailyHodl
cryptocurrency = cryptocurrency_scraper.cryptocurrency

eel.init("web")

@eel.expose
def config(query, amount, resources):

    #checks which resourses user has selected
    if "1" in resources:
        cryptocurrency_info = cryptocurrency(query, amount)
    if "2" in resources:
        daily_hold_info = dailyHodl(query, amount)

    #adding all necessary variables
    all_text = []
    titles = []
    srcs = []
    queries = query.split()

    #summarises amount of found articles form each resource
    if "1" in resources and "2" in resources:
        total_counter = daily_hold_info[3] + cryptocurrency_info[3]
        counter = daily_hold_info[3]
    
    #assigns amount of found articles form first resource only
    elif "1" in resources:
        total_counter = cryptocurrency_info[3]
        counter = cryptocurrency_info[3]
    
    #assigns amount of found articles form second resource only
    elif "2" in resources:
        total_counter = daily_hold_info[3]
        counter = daily_hold_info[3]

    #for amount of found articles in resource
    for i in range(counter):
        
        #checks if resource 1 has been selected
        if "1" in resources:

            #adds all information of each article from resource 1
            titles.append(cryptocurrency_info[0][i])
            srcs.append(cryptocurrency_info[1][i])
            all_text.append(cryptocurrency_info[2][i])

        #checks if resource 2 has been selected
        if "2" in resources:

            #adds all information of each article from resource 2
            srcs.append(daily_hold_info[1][i])
            all_text.append(daily_hold_info[2][i])
            titles.append(daily_hold_info[0][i])

    #returns all information
    return titles, srcs, all_text, total_counter, queries
    
eel.start("index.html", size = (1500, 900))