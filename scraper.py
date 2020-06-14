import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd


logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def read_raw_data(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('span', attrs={'class': 'short-desc'})
        return data

    def save_raw_data(self, data):
        with open('scrapped_data.txt', 'w') as f:
            for found in data:
                f.write(found.prettify())

    def append_data(self, data, record):
        date = record.find('strong').text[0:-1] + ', 2017'
        lie = record.contents[1][1:-2]
        explanation = record.find('a').text[1:-1]
        url = record.find('a')['href']
        data.append(
            {
                'date': date, 'lie': lie, 'explanation': explanation, 'url': url
            }
        )

        return data

    def save_csv(self, data):
        df_data = []
        for row in data:
            df_data.append([row.property_1, row.property_2, row.property_3, row.property_4])
        df = pd.DataFrame(df_data, columns=['property_1', 'property_2', 'property_3', 'property_4'])
        df['property_1'] = pd.to_datetime(df['property_1'])
        df.to_csv('data.csv', index=False, encoding='utf-8')

    def scrape(self):
        """ Gives the text from the website """

        url = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'
        response = requests.get(url)


        if not response.ok:
            # log the error
            logger.error(response.text)

        else:
            data = self.read_raw_data(response)
            self.save_raw_data(data)
            return data
