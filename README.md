![stars](https://img.shields.io/github/stars/Brondee/Scraper?color=blue&style=flat-square)
![downloads](https://img.shields.io/github/downloads/Brondee/Scraper/total?color=pink&style=flat-square)
![top_lang](https://img.shields.io/github/languages/top/Brondee/Scraper?style=flat-square)
![activity](https://img.shields.io/github/commit-activity/y/Brondee/Scraper?color=red&style=flat-square)

<h1 align = "center">Python Selenium Scraper with Web interface</h1>

<img src = "project_screenshots/main-img2.png?raw=true" align = "center">

# 📝 Descrtiption
I'm new with python and have decided to create this interesting project, because I want to practice and learn something new, in this case - `Selenium`.
This scraper parses only two websites ([Currency.com](https://currency.com/), [The Daily Hodl](https://dailyhodl.com/)), but can parse more if you add more python scrapers(scripts) to `scrapers` folder in project directory. To connect python functions with web interface I used `eel`. Scraper's really slow, but I will probably make it faster later.

# ⚙️ Functionality 
![Alt text](project_screenshots/functionality2.png?raw=true "Title")
## Search
In this sreenshot there is a search input, where user writes some queries, if there more than one query, user should type them with space between each word. For example,
user want to search for dogecoin and litecoin, he should type in input: "dogecoin litecoin".
## Amount of articles 
On the right side of the search input, there is an input for amount of articles to return using each query and from each resource(website). User should type there number between 1 to 9. For example, if user will type "dogecoin litecoin" in search and "1" in amount input, it will return 4 articles(1 for each query and for each website).
## Resources chooser
Underneath the search input, there are two buttons. If you click on the left one, you will choose [Currency.com](https://currency.com/) website to scrape, if you click on the right one, you will choose [The Daily Hodl](https://dailyhodl.com/) website. You can choose both. P.S. [Currency.com](https://currency.com/) scraper is much faster than [The Daily Hodl](https://dailyhodl.com/) one.
## Pre-choice query
Below the resources chooser, there are four buttons. Each button has it's own text. If you click on a button, it will insert it's text value to search input, so you don't need to type it by yourself. For example, user clicks on the first button "Ethereum", it inserts "Ethereum" to search input.
## Submit
By filling in values in search, amount and choosing resource, just click on submit, script will automatically get all information from websites.

# 🌀 Results
![Alt text](project_screenshots/results.png?raw=true "Title")
____
Python scrypt returns all information about articles to js scrypt, and it creates new block for each article. Js also groups articles by query, so it becomes musch easier to navigate. User can hide and show all articles in each group by clicking on "group" button.

# 🕹 Project setup
As I have mentioned before, I used `Selenium` and `eel`, so if you don't have them installed, use commands below:
```python
pip install selenium
```
```python
pip install eel
```
Also you can download `chromedriver` here:
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
