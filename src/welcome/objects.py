import random

class Dice(object):
    def __init__(self, n_faces):
        self.n_faces = n_faces


    def roll(self):
        self.result = random.randint(1, self.n_faces)
        return self.result
