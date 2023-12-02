"""Stores all big variables."""
import os

os.environ['OPENAI_API_KEY'] = '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'

movie_list: list[str] = ["The Shawshank Redemption", "The Godfather", "Titanic", "Star Wars: Episode IV - A New Hope", "Jurassic Park", "Avatar", 
             "Harry Potter", "Forrest Gump", "Inception", "The Matrix", "Pulp Fiction", 
             "The Lord of the Rings: The Fellowship of the Ring", "Fight Club", "The Dark Knight", "Schindler's List", "Toy Story", "Saving Private Ryan",
             "Amélie", "The Lion King", "Gladiator", "Parasite", "La La Land", "The Silence of the Lambs", "Interstellar", "Spirited Away"]

system_content_select_character: str = "You are a movie expert and you need to randomly select a character from a given movie."

system_content_clue: str = "I am playing a game like 20Q but there is only 3 clues and it is about guessing movie characters. The clue ordered from most difficult to relatively easy. You are the person who give out the clue. I will provide you the name of the movie and the chosen character, you need to give me the clue followed by instruction."


def ask_for_character(movie: str) -> str:
    ask_for_character: str = f"Please randomly select A character in the movie {movie}. Please return to me ONLY the name without any other content and information."
    return ask_for_character


def first_clue(ask_for_character: str, movie: str) -> str:
    first_clue: str = f"This is the first clue which has the highest difficulty level. Please give me the distinct physical features of the {ask_for_character} in the movie {movie}. Never mention the name of the character in your clue! This clue should be only in one concise sentence. Do not include any instructions to the game, just return the clue itself is enough."
    return first_clue


def second_clue(ask_for_character: str, movie: str) -> str:
    second_clue: str = f"This is the second clue which is the medium difficulty level. Please give me the distinct actions or the personality of the {ask_for_character} in the movie {movie}. Never mention the name of the character in your clue! This clue should be only in one concise sentence. Do not include any instructions to the game, just return the clue itself is enough."
    return second_clue


def third_clue(ask_for_character: str, movie: str) -> str:
    second_clue: str = f"This is the third clue which is the relatively easy. Please give me the role of {ask_for_character} in the movie {movie}. Never mention the name of the character in your clue! This clue should be only in one concise sentence. Do not include any instructions to the game, just return the clue itself is enough."
    return second_clue