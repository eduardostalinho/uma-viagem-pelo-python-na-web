import random
import hug

@hug.get("/")
def welcome(name:hug.types.text="Grupy-PR"):
    return "Welcome to {}!".format(name)


@hug.get("/dice/")
def welcome(sides: hug.types.number=6):
    return random.randint(1, sides)
