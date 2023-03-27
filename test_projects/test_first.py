

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_lauch(setup):
    print("pass")


def test_good():
    print("hello piyush")

@pytest.mark.smoke
def test_none():
    print("no one out")

