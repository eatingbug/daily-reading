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


def extract_geeknews(soup):
    """
    BeautifulSoup Object에서 GeekNews 데이터를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """
    upload_contents = '## GeekNews\n\n'
    url_prefix = "https://news.hada.io/"
    topics = soup.select("body > main > article > div.topics > div.topic_row")
    index = 0

    for topic in topics:
        if index >= 30:
            break

        title = topic.select_one("div.topictitle > a > h1").text.strip()
        link = topic.select_one("div.topicdesc > a")['href']
        description = topic.select_one("div.topicdesc > a").text.strip()

        index += 1

        upload_content = (
            f'<a href="{url_prefix}{link}">{index}. {title}</a><br/>\n'
            f'```md\n'
            f'{description}\n'
            f'```\n'
        )
        upload_contents += upload_content

    return upload_contents
