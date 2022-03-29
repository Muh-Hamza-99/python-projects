import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

def get_url(position, location):
    template_url = "https://www.indeed.com/jobs?q={}&l={}"
    url = template_url.format(position, location)
    return url

url = get_url("accountant", "canada")
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
job_cards = soup.find_all("div", class_="job_seen_beacon")
card = job_cards[0]

def get_record():
    job_title = card.h2.span.get("title")
    company_details = card.find("span", class_="companyName").a
    company_name = company_details.text
    base_url = "https://www.indeed.com"
    company_link = base_url + company_details.get("href")
    date_posted = card.find("span", class_="date").text.replace("Posted", "")
    today_date = datetime.today().strftime("%Y-%m-%d")
    print(today_date)

get_record()