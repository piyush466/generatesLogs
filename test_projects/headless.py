from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
obje_serv = Service()
driver = webdriver.Chrome(service=obje_serv,options=chrome_options)
driver.get("https://www.amazon.in/")
print("passs")

