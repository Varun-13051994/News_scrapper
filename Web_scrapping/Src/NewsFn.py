
def news_extract(news_link):

    import requests as rq
    from bs4 import BeautifulSoup as bs

    news_url = news_link
    
    response_news = rq.get(news_url)
    
    soup_news = bs(response_news.text, "html.parser")
    
    container_news = soup_news.find_all("div", class_ = "cmp-text")
    newslist = []
    for news_sections in container_news:
        newslist.append(news_sections.text.strip())
    
    full_news = "\n".join(newslist)
    
    return full_news

