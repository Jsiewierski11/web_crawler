import requests
import lxml
from xlwt import *
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.rottentomatoes.com/top/bestofrt/"
    f = requests.get(url)
    # print(f)

    soup = BeautifulSoup(f.content, 'lxml')

    movies = soup.find('table', {'class': 'table'}).find_all('a')
    # print(movies)

    movies_lst = []
    num = 0
    for anchor in movies:
        urls = "https://www.rottentomatoes.com" + anchor['href']
        movies_lst.append(urls)
        num += 1
        movie_url = urls
        movie_f = requests.get(movie_url)
        movie_soup = BeautifulSoup(movie_f.content, 'lxml')
        movie_content = movie_soup.find('div', {'class': 'movie_synopsis clamp clamp-6 js-clamp'})
        print(f"{num} {urls} \n Movie: {anchor.string.strip()}")
        print(f"Movie info: {movie_content.string.strip()}")
