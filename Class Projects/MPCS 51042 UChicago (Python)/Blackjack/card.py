import os
import tkinter as tk
from PIL import ImageTk, Image

 
class Card:
    
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"
    card_images = {}
    card_values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}


    def __init__(self, suit, value):
        self._suit = suit
        self._value = value


    @classmethod
    def load_images(cls):
        list_of_values_opening_file = list(range(2, 11)) + ["A", "J", "K", "Q"]
        list_of_club_attributes = [cls.CLUBS, cls.DIAMONDS, cls.HEARTS, cls.SPADES]
        
        for club_attribute in list_of_club_attributes:
            for value_file in list_of_values_opening_file:
                file_path = os.path.join(os.path.join(os.path.dirname(__file__), "images"), f"{value_file}{club_attribute[0].upper()}.jpg")
                image = Image.open(file_path)
                image = image.resize((90, 140))
                image = ImageTk.PhotoImage(image)
                cls.card_images[tuple([club_attribute, value_file])] = image


    @property
    def value(self):
        numerical_value = Card.card_values[self._value]
        return numerical_value


    @property
    def image(self):
        tuple_of_requested_card = tuple([self._suit, self._value])
        requested_card_image_object = Card.card_images[tuple_of_requested_card]
        return requested_card_image_object