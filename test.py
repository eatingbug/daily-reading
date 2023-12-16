from crawling import extract_news_data, parsing_beautifulsoup


if __name__ == "__main__":
    
    business_news_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"

    soup = parsing_beautifulsoup(business_news_url)
    contents = extract_news_data(soup)

    print(contents)