"""Stores all big variables."""
import os

os.environ['OPENAI_API_KEY'] = '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'

movie_list: list[str] = ["The Shawshank Redemption", "The Godfather", "Titanic", "Star Wars: Episode IV - A New Hope", "Jurassic Park", "Avatar", 
             "Harry Potter and the Sorcerer's Stone", "Forrest Gump", "Inception", "The Matrix", "Pulp Fiction", 
             "The Lord of the Rings: The Fellowship of the Ring", "Fight Club", "The Dark Knight", "Schindler's List", "Toy Story", "Saving Private Ryan",
             "Amélie", "The Lion King", "Gladiator", "Parasite", "La La Land", "The Silence of the Lambs", "Interstellar", "Spirited Away"]

system_content_select_character: str = "You are a movie expert and you need to randomly select a character from a given movie."

def ask_for_character(movie: str) -> str:
    ask_for_character: str = f"Please randomly select A character in the movie {movie}. Please return to me ONLY the name without any other content and information."
    return ask_for_character