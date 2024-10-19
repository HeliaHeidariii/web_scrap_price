from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


def arzdigital():
    site = 'https://arzdigital.com/coins/'
    response = requests.get(site).text
    soup = BeautifulSoup(response, 'html.parser')

    titles = soup.find_all('span', attrs={'class': "arz-tw-text-slate-400"})
    prices = soup.find_all(
        'span', attrs={'class': "arz-tw-text-xs arz-tw-mr-auto"})

    data = []
    for title, price in zip(titles, prices):
        data.append({
            'Title': title.get_text().strip(),
            'Price': price.get_text().strip(),
            'Source': 'Arzdigital'
        })
    return data


def tala():
    site = 'https://www.iranjib.ir/showgroup/23/realtime_price/'
    response = requests.get(site).text
    soup = BeautifulSoup(response, 'html.parser')

    titles = soup.find_all('a', attrs={'class': "tts"})
    prices = soup.find_all('span', attrs={'class': "lastprice"})

    data = []
    for title, price in zip(titles, prices):
        data.append({
            'Title': title.get_text().strip(),
            'Price': price.get_text().strip(),
            'Source': 'Iranjib'
        })
    return data


def save_to_csv(data):
    date_today = datetime.now().strftime('%Y-%m-%d')
    filename = 'prices_data_edit3.csv'

    fields = ['Date', 'Title', 'Price', 'Source']

    with open(filename, mode='a', newline='', encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if file.tell() == 0:
            writer.writeheader()

        for item in data:
            writer.writerow(
                {'Date': date_today, 'Title': item['Title'], 'Price': item['Price'], 'Source': item['Source']})


arzdigital_data = arzdigital()
tala_data = tala()


all_data = arzdigital_data + tala_data


save_to_csv(all_data)
