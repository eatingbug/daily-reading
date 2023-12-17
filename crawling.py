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


def extract_news_data(soup):
    """
    BeautifulSoup Object에서 news data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    news_posts = soup.select(".PO9Zff")
    url_prefix = "https://news.google.com"
    print(len(news_posts))
    index = 0

    for news in news_posts:
        if index >= 30:
            break

        news = news.select("c-wiz > div > article > a")
        if news == []:
            continue

        news_name = news[0].text
        url_suffix = news[0].attrs['href']
        news_link = url_prefix + url_suffix[1:]
        index += 1
        
        content = f'<a href="{news_link}">{index}. {news_name}</a><br/>\n'
        print(content)
        upload_contents += content

    return upload_contents