import requests
from bs4 import BeautifulSoup


# seed url: https://www.apache.org/

seed_url = "https://www.apache.org/"
visted_urls = [] # Can change to set to speed it up
# urls_to_visit = []

req = requests.get(seed_url)
visted_urls.append(seed_url)

# print(req.text)
print(seed_url)

def get_links(req):
    soup = BeautifulSoup(req.text, 'lxml')
    links = soup.find_all('a')
    urls_to_visit = []
    
    for link in links:
        text_url = link.get('href')
        if text_url is not None:
            if text_url.startswith('http'):
                print(f'\t{text_url}')
                if text_url not in visted_urls:
                    urls_to_visit.append(text_url)


    for link in urls_to_visit:
        if link not in visted_urls:
            req = requests.get(link)
            if link.startswith('http'):
                visted_urls.append(link)
                print(link)
                get_links(req)

get_links(req)
        


