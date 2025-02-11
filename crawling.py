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
    news_posts = soup.select("#contentarea_left > div.mainNewsList._replaceNewsLink > ul > li")
    url_prefix = "https://finance.naver.com/"
    print(len(news_posts))
    index = 0

    for news in news_posts:
        if index >= 30:
            break

        news_name = news.select_one("dd.articleSubject > a").text
        url_suffix = news.select_one("dd.articleSubject > a")['href']
        news_link = url_prefix + url_suffix[1:]
        content = news.select_one("dd.articleSummary").text.strip()
        content = content.replace('\n', '').replace('\t', '').replace('  ', ' ')
        content = content.split('|')[0].strip()
        index += 1

        upload_content = f'<a href="{news_link}">{index}. {news_name}</a><br/>\n{content}<br/>\n'
        upload_contents += upload_content

    return upload_contents
