from bs4 import BeautifulSoup
import requests


def parsing_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. Google News Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url)

    html = data.text
    return BeautifulSoup(html, 'html.parser')


def extract_book_data(soup):
    """
    BeautifulSoup Object에서 news data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    new_books = soup.select(".goodsTxtInfo")
    url_prefix = "http://www.yes24.com"

    return upload_contents