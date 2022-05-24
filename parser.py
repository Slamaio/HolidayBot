import requests
from bs4 import BeautifulSoup as BS

from config import headers, importance



class Parser:
    def __init__(self, url, headers: dict = headers) -> None:
        self.headers = headers
        self.url = url
        self.r = requests.get(url, headers=headers)
        self.html = BS(self.r.content, 'html.parser')


    def getDate(self) -> str:
        """
        Returns current date
        """
        date = self.html.find('h2', class_='mainpage').text
        return date
        

    def getHolidays(self, level: int = 0) -> list:
        """
        Returns a list of holidays depending on their importance
        """
        holidays = []
        for holiday in self.html.find_all('div', {'itemprop':importance[level][1]}):
            holiday_name = holiday.find('span', {'itemprop':'text'})
            holidays.append(holiday_name.text)
        return holidays