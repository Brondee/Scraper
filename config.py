import eel
from daily_hold_scraper import dailyHold
from cryptocurrency_scraper import cryptocurrency

eel.init("web")

@eel.expose
def config(query, amount, resources):

    if "1" in resources:
        cryptocurrency_info = cryptocurrency(query, amount)
    if "2" in resources:
        daily_hold_info = dailyHold(query, amount)

    all_text = []
    titles = []
    srcs = []
    queries = query.split()

    if "1" in resources and "2" in resources:
        total_counter = daily_hold_info[3] + cryptocurrency_info[3]
        counter = daily_hold_info[3]
    elif "1" in resources:
        total_counter = cryptocurrency_info[3]
        counter = cryptocurrency_info[3]
    elif "2" in resources:
        total_counter = daily_hold_info[3]
        counter = daily_hold_info[3]

    for i in range(counter):
        
        if "1" in resources:
            titles.append(cryptocurrency_info[0][i])
            srcs.append(cryptocurrency_info[1][i])
            all_text.append(cryptocurrency_info[2][i])

        if "2" in resources:
            srcs.append(daily_hold_info[1][i])
            all_text.append(daily_hold_info[2][i])
            titles.append(daily_hold_info[0][i])

    return titles, srcs, all_text, total_counter, queries

eel.start("index.html", size = (1500, 900))