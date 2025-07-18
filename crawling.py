import json
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver():
    options = Options()
    options.add_argument('--headless')  # 창을 띄우지 않음
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    return driver


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


def extract_finance_news(soup):
    """
    BeautifulSoup Object에서 Finance News 데이터를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """
    upload_contents = '## Finance News\n\n'
    # 리스트 아이템들을 모두 선택 (상대경로, 태그 위주)
    
    json_text = soup.get_text()
    json_data = json.loads(json_text)

    summary = json_data.get('data', {}).get('summary', '')

    index = 0
    for item in summary:
        title = item.get('header', '').strip()
        content = item.get('detail', '').strip()

        index += 1

        upload_content = (
            f'{index}. {title}\n'
            f'`{content}`\n'
        )
        upload_contents += upload_content

    return upload_contents