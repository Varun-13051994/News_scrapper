import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
from Src.NewsFn import news_extract


url_hw = r"https://www.honeywell.com/in/en/press"


response = rq.get(url_hw)

text_response = response.text

soup = bs(text_response, features = "html.parser")
    
container = soup.find("div", class_ = "list-component mvp2 articlegrid")
count = 1
datalist = []


for items in container.find_all("li", class_ = "data-list__item"):
    
    date_tag = items.find("span", class_ = "list-component__item-displaydate")
    date = date_tag.text.strip().replace("|", "") if date_tag else None

    title = items.find("div", class_ = "list-component__item-headline").text.strip()
    
    link_tag = items.find_all("a", href = True)[1]
    link = ''.join([r"https://www.honeywell.com", link_tag["href"]])

    news_extracted = news_extract(link)
    
    datalist.append([title, date, link, news_extracted])
    
    count += 1
    if count > 20:
        break
    continue

df = pd.DataFrame(data=datalist, columns = ['Article title', 'Published date', 'Link', 'Full_news_extract'])

df['Published date'] = pd.to_datetime(df['Published date'], format = "mixed")

df.to_csv(r"C:\Users\sumithras\OneDrive\Desktop\Honeywell_news.csv", index = False)

print('Export of news article is successful! 🥂😀')