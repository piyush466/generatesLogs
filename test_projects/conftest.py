import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    obj_serv = Service()
    driver = webdriver.Chrome(service=obj_serv)
    driver.get("https://www.facebook.com/LighterDreamBariatricSurgery/")
    yield
    driver.close()




