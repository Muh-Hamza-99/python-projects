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
soup = BeautifulSoup(driver.page_source, "html.parser")

def extract_record(item):
    anchor_tag = item.h2.a
    product_title = anchor_tag.text
    url = "https://www.amazon.com" + anchor_tag.get("href")
    price_tag = item.find("span", "a-price")
    price = price_tag.find("span", "a-offscreen").text
    rating = item.i.text
    review_count = item.find("span", { "class": "a-size-base", "dir": "auto" }).text
    result = (product_title, url, price, rating, review_count)
    return result

records = []
results = soup.find_all("div", { "data-component-type": "s-search-result" })
for item in results:
    records.append(extract_record(item))