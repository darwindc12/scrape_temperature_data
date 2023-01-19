import selectorlib
import requests
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

def scrape(url):
    scrape_local = requests.get(url)
    result = scrape_local.text
    return result


def extract(scrape_local):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(scrape_local)["tours"]
    return value


# def read(temp):
#     cursor.execute("SELECT * FROM Climate WHERE Date=?, Temperature", temp)
#     rows = cursor.fetchall()
#     return rows


def store(extracted_local):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    row = cursor.execute("INSERT INTO Climate VALUES(?,?)", (now, extracted_local))
    connection.commit()
    print("Temperature was successfully inserted")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    # print(extracted)
    store(extracted)