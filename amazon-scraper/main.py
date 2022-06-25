from selenium import webdriver
from bs4 import BeautifulSoup
import csv

def get_url(search_term):
    template = "https://www.amazon.com/s?k={}"
    search_term = search_term.replace(" ", "+")
    url = template.format(search_term)
    url += "&page={}"
    return url

def extract_record(item):
    anchor_tag = item.h2.a
    product_title = anchor_tag.text
    url = "https://www.amazon.com" + anchor_tag.get("href")
    try:
        price_tag = item.find("span", "a-price")
        price = price_tag.find("span", "a-offscreen").text
    except AttributeError: 
        return
    try:
        rating = item.i.span.text
        review_count = item.find("span", { "class": "a-size-base" }).text
    except AttributeError:
        rating = ""
        review_count = ""
    result = (product_title, url, price, rating, review_count)
    return result

def main(search_term):
    driver = webdriver.Firefox()
    records = []
    url = get_url(search_term)
    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find_all("div", { "data-component-type": "s-search-result" })
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    driver.close()
    with open("results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Title", "URL", "Price", "Rating", "Review Count"])
        writer.writerows(records)

main("keyboard")