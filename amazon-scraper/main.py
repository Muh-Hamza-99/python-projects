from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Firefox()
url = "https://www.amazon.com"
driver.get(url)