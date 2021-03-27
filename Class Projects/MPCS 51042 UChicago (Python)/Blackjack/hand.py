import tkinter as tk
from card import Card


class Hand:
    
    def __init__(self):
        self.collection_of_cards = []


    def reset(self):
        self.collection_of_cards = []


    def add(self, card):
        self.collection_of_cards.append(card)


    @property
    def total(self):
        sum_values = 0
        for card_object in self.collection_of_cards:
            sum_values += card_object.value
        return sum_values


    def draw(self, canvas, start_x, start_y, canvas_width, canvas_height):
        for index, card_object in enumerate(self.collection_of_cards):
            canvas.create_image(start_x + index * 100, start_y, anchor = "nw", image = card_object.image)
