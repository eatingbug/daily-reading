import os
from datetime import datetime

from zoneinfo import ZoneInfo
from crawling import extract_geeknews, parsing_beautifulsoup
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "daily-reading"

    seoul_timezone = ZoneInfo('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    parsing_url = "https://news.hada.io/past"
    soup = parsing_beautifulsoup(parsing_url)
    upload_contents = extract_geeknews(soup)

    issue_title = f"{today_date}_뉴스"
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
