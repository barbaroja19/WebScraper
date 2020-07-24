from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
import time
from bs4 import BeautifulSoup

URL ='http://books.toscrape.com'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

bookTitle = soup.find('h3', attrs={'title'})

print(bookTitle)






