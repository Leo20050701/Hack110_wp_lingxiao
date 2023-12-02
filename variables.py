"""Stores all big variables."""
import os

os.environ['OPENAI_API_KEY'] = ''

movie_list: list[str] = ["The Shawshank Redemption", "The Godfather", "Titanic", "Star Wars: Episode IV - A New Hope", "Jurassic Park", "Avatar", 
             "Harry Potter and the Sorcerer's Stone", "Forrest Gump", "Inception", "The Matrix", "Pulp Fiction", 
             "The Lord of the Rings: The Fellowship of the Ring", "Fight Club", "The Dark Knight", "Schindler's List", "Toy Story", "Saving Private Ryan",
             "Amélie", "The Lion King", "Gladiator", "Parasite", "La La Land", "The Silence of the Lambs", "Interstellar", "Spirited Away"]

system_content_select_character: str = "You are a movie expert and you need to randomly select a character from a given movie."

system_content_clue: str = "I am playing a game like 20Q but there is only 3 clues and it is about guessing movie characters. The clue ordered from most difficult to relatively easy. You are the person who give out the clue. I will provide you the name of the movie and the chosen character, you need to give me the clue followed by instruction."

def ask_for_character(movie: str) -> str:
    ask_for_character: str = f"Please randomly select A character in the movie {movie}. Please return to me ONLY the name without any other content and information."
    return ask_for_character