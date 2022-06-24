from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Firefox()

def get_url(search_term):
    template = "https://www.amazon.com/s?k={}"
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)

url = get_url("monitor")
driver.get(url)