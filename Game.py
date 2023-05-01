from Quiz import *
from pickle import dump, load
from os import stat

class Game:
    def __init__(self):
        with open(r"quizes.txt", "rb") as data:
            if stat(r"quizes.txt").st_size != 0:
                self.quizes = load(data)
            else: self.quizes = []

    def create_quiz(self):
        new_quiz = Quiz()
        self.quizes.append(new_quiz)

    def delete_quiz(self, quiz: Quiz):
        self.quizes.remove(quiz)

    def save_quizes(self):
        with open(r"quizes.txt", "wb") as data:
                dump(self.quizes, data)