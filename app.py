
from random import random

from flask import Flask, render_template, request


class the_game:
    def __init__(self):
        self.tot_wins = 0
        self.tot_ties = 0
        self.tot_loses = 0
        self.computer_wins = 0
        self.options = ['Rock', 'Paper', 'Scissors']
        self.player_choice = None
        self.computer_choice = None
        self.winner = None

    def player_choice(self,choice):
        self.player_choice = choice

    def computer_choice(self):
        self.computer_choice = random.choice(self.options)

    def det_winner(self):
        if self.player_choice == self.computer_choice:
            self.tot_ties += 1
        elif (self.player_choice == 'Rock' and self.computer_choice == 'Paper') or\
            (self.player_choice == 'Scissors' and self.computer_choice == 'Rock') or\
            (self.player_choice == 'Paper' and self.computer_choice == 'Scissors'):
            self.tot_wins += 1
        else:
            self.tot_loses += 1
            self.computer_wins += 1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result')
def result():
    ret_val = request.args.get('id')

    if not ret_val:
        ret_val = 'No ID provided'

    return render_template("results.html", ret_val=ret_val)

@app.route('/comresult')
def computerresult():
    comret_val = 'rock'

    if not comret_val:
        comret_val = 'No ID provided'

    return render_template("results.html", comret_val=comret_val)

def total_wins():
    ret_score = request.args.get('score')

if __name__ == '__main__':
    app.run(debug=True)
