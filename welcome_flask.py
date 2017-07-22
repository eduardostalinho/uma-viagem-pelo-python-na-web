import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    '''Says welcome'''
    return "Welcome to Grupy-PR!"

@app.route('/dice/')
def dice_roll():
    '''Rolls a dice'''
    return str(random.randint(1, 6))
