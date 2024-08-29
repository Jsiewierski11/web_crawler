import requests
import lxml
from xlwt import *
from bs4 import BeautifulSoup
from transformers import pipeline

def get_initial_movie_data(movie_name: str) -> dict:
    url = f"https://www.rottentomatoes.com/search?search={movie_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    movie_url = soup.find('search-page-media-row').get('href')
    movie_page = requests.get(f"https://www.rottentomatoes.com{movie_url}")
    movie_soup = BeautifulSoup(movie_page.content, 'lxml')
    summary = movie_soup.find('div', {'class': 'movie_synopsis'}).text.strip()
    reviews = [review.text.strip() for review in movie_soup.find_all('blockquote')]
    runtime = movie_soup.find('time').text.strip()
    return {
        'url': movie_url,
        'summary': summary,
        'reviews': reviews,
        'runtime': runtime
    }

def get_movie_info_from_llm(movie_name: str, initial_data: dict, llm_choice: str) -> dict:
    if llm_choice == 'llama':
        model_name = 'meta-llama/Meta-Llama-3.1-8B'
    elif llm_choice == 'mistral':
        model_name = 'mistralai/Mistral-Large-Instruct-2407'
    else:
        raise ValueError("Unsupported LLM choice")

    generator = pipeline('text-generation', model=model_name)
    prompt = (
        f"Using the following initial data about the movie {movie_name}:\n"
        f"Summary: {initial_data['summary']}\n"
        f"Reviews: {initial_data['reviews']}\n"
        f"Runtime: {initial_data['runtime']}\n"
        "Provide a detailed summary, additional reviews, runtime, reasons to watch, and recommend similar movies."
    )
    response = generator(prompt, max_length=500)
    return response[0]['generated_text']

if __name__ == "__main__":
    movie_name = input("Enter the movie name: ").strip()
    llm_choice = input("Enter the LLM to use (llama/mistral): ").strip().lower()
    if movie_name and llm_choice:
        initial_data = get_initial_movie_data(movie_name)
        movie_info = get_movie_info_from_llm(movie_name, initial_data, llm_choice)
        print(f"Summary: {movie_info['summary']}")
        print(f"Reviews: {movie_info['reviews']}")
        print(f"Runtime: {movie_info['runtime']}")
        print(f"Reasons to Watch: {movie_info['reasons_to_watch']}")
        print(f"Recommendations: {movie_info['recommendations']}")
    else:
        print("Please enter a valid movie name and LLM choice.")