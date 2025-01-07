from crawling import extract_news_data, parsing_beautifulsoup


if __name__ == "__main__":
    
    business_news_url = "https://finance.naver.com/news/mainnews.naver"

    soup = parsing_beautifulsoup(business_news_url)
    contents = extract_news_data(soup)

    print(contents)