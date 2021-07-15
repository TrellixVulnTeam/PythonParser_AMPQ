import requests
from bs4 import BeautifulSoup


def get_data(url):
  headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }

  req = requests.get(url, headers)
  print(req.text)

get_data("https://www.hammonia-reederei.de/news-1?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=74&cHash=2b1869f298ef95f48d7a11902ffd4618")

