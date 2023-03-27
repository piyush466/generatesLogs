from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# test = Service(r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
#
#
# driver = webdriver.Chrome(service=test)

driver = webdriver.Firefox(executable_path=r"C:\\Users\\Cliffex-Lead\\Desktop\\test\\firefox\\geckodriver-v0.32.2-win32\\geckodriver.exe")
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
