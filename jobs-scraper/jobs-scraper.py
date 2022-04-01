import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    template = "https://www.indeed.com/jobs?q={}&l={}"
    url = template.format(position, location)
    return url

def get_record(card):
    job_title = card.h2.span.get("title")
    job_company_name = card.find("span", class_="companyName").text
    job_company_location = card.find("div", class_="companyLocation").text
    job_post_date = card.find("span", class_="date").text.replace("Posted", "")
    today = datetime.today().strftime("%Y-%m-%d")
    job_summary = card.find("div", class_="job-snippet").ul.text.strip().replace("\n", "")
    record = (job_title, job_company_name, job_company_location, job_post_date, today, job_summary)
    return record

def main(position, location):
    records = []
    url = get_url(position, location)
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        cards = soup.find_all("div", "job_seen_beacon")
        for card in cards:
            record = get_record(card)
            records.append(record)
        try:
            url = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get("href")
        except AttributeError:
            break
    with open("sample-data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "PostDate", "ExtractDate", "Summary"])
        writer.writerows(records)

main("senior accountant", "charlotte nc")