import os
from datetime import datetime

from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
from crawling import fetch_finance_news, extract_geeknews, get_chrome_driver, parsing_beautifulsoup
from github_utils import get_github_repo, upload_github_issue
from selenium_stealth import stealth


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "daily-reading"

    seoul_timezone = ZoneInfo('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    finance_contents = fetch_finance_news()

    driver = get_chrome_driver()

    stealth(driver,
        languages=["ko-KR", "ko"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    parsing_url = "https://news.hada.io/past"
    soup = parsing_beautifulsoup(parsing_url)
    geeknews_contents = extract_geeknews(soup)

    upload_contents = finance_contents + '\n' + geeknews_contents
    issue_title = f"{today_date}_뉴스"
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
