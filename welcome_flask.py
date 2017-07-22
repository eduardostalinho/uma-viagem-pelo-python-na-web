import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Grupy-PR!"

@app.route('/dice/')
def dice_roll():
    return str(random.randint(1, 6))
