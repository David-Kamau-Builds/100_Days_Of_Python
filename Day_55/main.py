import random
from flask import Flask
app = Flask(__name__)

target_number = random.randint(0, 9)

@app.route("/")
def home():
    return ('<h1 style="text-align: center; margin-top: 9rem;">Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDg0MXhzODc0YW9ucjQzaHU3OXlnYWpyNTQzMmZ4cnBiczBmZDM0cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l378khQxt68syiWJy/giphy.gif"'
            'style="display:block; margin:auto; width:50%;">')

@app.route("/<int:guess>")
def check_guess(guess):
    if guess > target_number:
        return ('<h1 style="text-align: center; margin-top: 9rem;">The guess is too high!!</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bWx0bGo1cWdkcjRwcnZxdGdqM3k0cHB3MmoxaWtoeHF3Yzc2MzN4ciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SyemapFxj7TiM/giphy.gif"'
            'style="display:block; margin:auto; width:50%;">')

    elif guess < target_number:
        return ('<h1 style="text-align: center; margin-top: 9rem;">The guess is too low!!</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDE5eXNib3Fta2ZjbWpqd2owcGk5dHJwNTdyNzJ0YmRtd2JwbWl6NSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BaXZhPYWMJ1nWfbSk6/giphy.gif"'
            'style="display:block; margin:auto; width:50%;">')

    else:
        return (f'<h1 style="text-align: center; margin-top: 9rem;">You got it. the number is {target_number}</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZHRvZG14OG5taDRkMzZneGQxcDB5bm1rczEwMXZzamxybm9vcXA4byZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/m7x9ixXD8w5stcSBlc/giphy.gif"'
            'style="display:block; margin:auto; width:50%;">')



if __name__ == "__main__":
    app.run(debug=True)
    
