"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather
python3 -m main parse

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import sys
import logging
import requests
from bs4 import BeautifulSoup

from scraper import Scraper
from storage import Persistor
from myparser import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = 'scrapped_data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather():
    logger.info("gather")

    scrapper = Scraper(Persistor)
    scrapper.scrape()


def parse():
    # parse gathered data and save as csv

    logger.info("parse")
    scrapper = Scraper(Persistor)
    parser = Parser()
    raw_data = scrapper.scrape()

    data = []
    for raw in raw_data:
        data = scrapper.append_data(data, raw)
    parsed_files = [parser.parse_object(file) for file in data]
    scrapper.save_csv(parsed_files)

    
if __name__ == '__main__':
    """
    What does the line above mean
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather()

    elif sys.argv[1] == 'parse':
        parse()

    logger.info("work ended")
