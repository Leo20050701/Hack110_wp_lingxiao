from openai import OpenAI
from variables import *
import os
import sys
import requests
from bs4 import BeautifulSoup


def get_response_from_AI(system_content: str, user_content: str) -> str:
    """Get the response from ChatGPT 4.0."""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
        {
            "role": "system", "content": f"{system_content}"
        },
        {
            "role": "user", "content": f"{user_content}"
        }
        ]
    )
    return response.choices[0].message.content


def get_first_bing_image_url(search_query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.bing.com/images/search?q={search_query}"

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        first_image = soup.find('a', class_='iusc')

        if not first_image:
            return "No image found."

        m = first_image.get('m')
        if not m:
            return "Image URL not found."

        start = m.find('murl')+7
        end = m.find('"', start)
        image_url = m[start:end]

        return image_url
    
    except Exception as e:
        return f"An error occurred: {e}"



"""print(get_first_bing_image_url("Pooh in Winnie the Pooh"))


movie: str = "Winnie the Pooh"
character: str = get_response_from_AI(system_content_select_character, ask_for_character(movie))
print(character)
print(f"Clue 1: {get_response_from_AI(system_content_clue, first_clue(character, movie))}")
print(f"Clue 2: {get_response_from_AI(system_content_clue, second_clue(character, movie))}")
print(f"Clue 3: {get_response_from_AI(system_content_clue, third_clue(character, movie))}")"""