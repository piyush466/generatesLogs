import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-certification-errors')

obj= Service()
driver = webdriver.Chrome(service=obj, chrome_options=chrome_options)
driver.get("https://moz.com/top500")
time.sleep(5)
list1 = []
items500 = driver.find_elements(By.XPATH,"//a[@class='text-nowrap']")

for item in items500:
    list1.append(item.text)

print(list1)
print(len(list1))

assert len(list1) == 500





