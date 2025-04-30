from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

'''
    1- This script logs in to the website
    2- clicking to the Homepage
    3- scraping temperature data
'''

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

def get_driver():
    options.add_argument("disable-infobars")                        #seleniumu engelleyecek info bar pop-ups
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')                   #linux makinalar icin
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])    #browser algısından kaçmak için
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")

    return driver

def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()

    # Fill in username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(0.5)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(0.5)

    # Click on Home link and wait 2 sec
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)

    # Scrape the temperature value
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

    return clean_text(element.text)

print(main())