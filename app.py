from flask import Flask, render_template, redirect, url_for, request
from variables import *
from W_o_W import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', movie_list=movie_list)

@app.route('/select_movie/<movie>')
def select_movie(movie):
    return redirect(url_for('game', movie=movie))

@app.route('/game/<movie>')
def game(movie):
    character = get_response_from_AI(system_content_select_character, ask_for_character(movie))
    clue = get_response_from_AI(system_content_clue, first_clue(character, movie))
    return render_template('game.html', movie=movie, character=character, round=1, clue=clue, message="", game_over=False)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    movie = request.form['movie']
    character = request.form['character']
    user_guess = request.form['guess']
    round = int(request.form['round'])

    # Compare user guess with the character name
    similarity = compare_strings(user_guess, character)
    win = similarity >= 40.0

    if win:
        message = f"You Win!! The correct answer is {character}"
        game_over = True
    else:
        round += 1
        if round > 4:
            message = f"You Loss... The correct answer was {character}"
            game_over = True
            clue = ""  # Ensure no clue is set on a loss
        else:
            message = f"Round {round} - Make another guess!"
            game_over = False

    if round == 1:
        clue = get_response_from_AI(system_content_clue, first_clue(character, movie))
    elif round == 2:
        clue = get_response_from_AI(system_content_clue, second_clue(character, movie))
    elif round == 3:
        clue = get_response_from_AI(system_content_clue, third_clue(character, movie))
    elif round == 4:
        image_url = get_first_bing_image_url(f"{character} in {movie}")
        clue = f"<img src='{image_url}' alt='Character Image Clue' class='round-four-image'>"


    return render_template('game.html', movie=movie, character=character, round=round, clue=clue, message=message, game_over=game_over)


if __name__ == '__main__':
    app.run(debug=True)
