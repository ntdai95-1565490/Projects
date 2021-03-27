import random
from card import Card


class Deck:
    
    def __init__(self):
        self.cards_in_deck = []
        list_of_values_opening_file = list(range(2, 11)) + ["A", "J", "K", "Q"]
        list_of_club_attributes = [Card.CLUBS, Card.DIAMONDS, Card.HEARTS, Card.SPADES]
        for card_value in list_of_values_opening_file:
            for club_value in list_of_club_attributes:
                instance_of_Card = Card(club_value, card_value)
                self.cards_in_deck.insert(random.randrange(len(self.cards_in_deck) + 1), instance_of_Card)
        self.card_have_dealt = []


    def deal(self):
        if len(self.cards_in_deck) == 0:
            self.shuffle()
        instance_of_top_card = self.cards_in_deck.pop()
        self.card_have_dealt.append(instance_of_top_card)
        return instance_of_top_card


    @property
    def size(self):
        number_of_cards_in_deck = len(self.cards_in_deck)
        return number_of_cards_in_deck


    def shuffle(self):
        random.shuffle(self.card_have_dealt)
        for instance_of_Card in self.card_have_dealt:
            self.cards_in_deck.insert(0, instance_of_Card)
        self.card_have_dealt = []