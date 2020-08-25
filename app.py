
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)


from flask import Flask 
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """Tells the user how much you like penguins"""
    return 'Penguins are cute!'
    
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user based on their favorite animal"""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user asking how their dessert was"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'{adjective} {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    return f"{number1} times {number2} is {int(number1) * int(number2)}."

@app.route('/sayntimes/<word>/<n>')
def words(word, n):
    x=''
    for _ in range(0, int(n)):
        x+= f'word '
    return x

@app.route('/reverse/<word>')
def reverse(word):
    reversedString=""
    index = len(str(word))
    while index > 0:
        reversedString += word [index-1]
        index = index -1
    return f'{reversedString}'

@app.route('/strangecaps/<word>')
def strangecaps(word):
    strangeWord=""
    for char in range(len(word)):
        if not char % 2 :
            strangeWord = strangeWord + word[char].upper()
        else:
            strangeWord = strangeWord + word[char].lower()
    return f'{strangeWord}'

@app.route('/dicegame')
def dicegame():
    return f"You rolled a {random.randint(1,6)}"

if __name__ == '__main__':
    app.run(debug=True)