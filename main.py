import os
from datetime import datetime

from pytz import timezone
from crawling import extract_news_data, parsing_beautifulsoup
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "news-reading"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    business_news_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"
    soup = parsing_beautifulsoup(business_news_url)
    upload_contents = extract_news_data(soup)

    issue_title = f"{today_date}_경제뉴스"
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")