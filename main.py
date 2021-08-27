import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import keyboard
from selenium.webdriver.common.keys import Keys


tenFastFinger_url = "https://10fastfingers.com/typing-test/turkish"
response_url = requests.get(tenFastFinger_url)
tenFastFinger_contents = response_url.content
soup = BeautifulSoup(tenFastFinger_contents,"html.parser")


browser = webdriver.Chrome('./chromedriver')
browser.get(tenFastFinger_url)



while True:
    try:
        if keyboard.is_pressed("9"):
            for i in range(5000):
                summ2 = browser.find_element_by_class_name("highlight").text
                elem = browser.find_element_by_class_name("form-control")
                elem.click()
                elem.send_keys(summ2)
                elem.send_keys(Keys.SPACE)
    except:
        break








