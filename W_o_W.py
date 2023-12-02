from openai import OpenAI
from variables import *
import os
import sys


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


def get_clue() -> str:
    return 
print(get_response_from_AI(system_content_select_character, ask_for_character("Star Wars")))