import selectorlib
import requests
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"


def scrape(url):
    scrape_local = requests.get(url)
    result = scrape_local.text
    return result


def extract(scrape_local):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(scrape_local)["tours"]
    return value


def read():
    with open("data.txt", 'r') as file:
        return file.read()


def store(extracted_local):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", 'a') as file:
        line = f"{now}, {extracted_local}" + "\n"
        file.write(line)
    print("Temperature was successfully inserted")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    # print(extracted)
    store(extracted)