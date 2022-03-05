from bs4 import BeautifulSoup
import requests
import json


def get_article_text(article):
    # go to article url
    url = article.get('href')    
    req = requests.get(url)

    # get article text
    soup = BeautifulSoup(req.text, 'lxml')
    article_text = soup.find('div', {'class': 'read__content'})
    
    return article_text.text[:1000] # first 1000 characters of article

def crawl_articles(url):
    result = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    articles = soup.find_all('a', {'class': 'article__link'})
    for article in articles:
        title = article.text
        text = get_article_text(article)
        print("############################################################################################")
        print(f"{title}\n{text}\n")

if __name__ == '__main__':
    url = 'http://indeks.kompas.com/news/2017-08-04/'
    crawl_articles(url)