import tkinter as tk
from abc import ABC, abstractmethod
from card import Card
from hand import Hand
from deck import Deck


class GameGUI(ABC):

    def __init__(self, window):
        self._window = window
        self._canvas_width = 1024
        self._canvas_height = 400
        self._canvas = tk.Canvas(window, width=self._canvas_width, height=self._canvas_height)
        self._canvas.pack()
        window.bind("<Key>", self._keyboard_event)

    def _keyboard_event(self, event):
        key = str(event.char)

        if key == 'h':
            self.player_hit()
        elif key == 's':
            self.player_stand()
        elif key == 'r':
            self.reset()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def player_hit(self):
        pass

    @abstractmethod
    def player_stand(self):
        pass


class BlackJack(GameGUI):

    game_status_text = ["In Progress...", 
                        "Player WINS... Press 'r' to start a new game",
                        "Dealer WINS... Press 'r' to start a new game",
                        "TIE Game...Press 'r' to start a new game"]
    game_status_text_colors = ["green", "red"]


    def __init__(self, window):
        super().__init__(window)
        self.player_wins = 0
        self.dealer_wins = 0
        self.game_status = None
        self.game_status_text_colors = None
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.cards_in_deck = Deck()
        self._canvas.create_text(self._canvas_width / 2, self._canvas_height / 2, anchor = tk.CENTER, text = f"Press r to start the game!", font = ('Arial', 50, 'bold italic'))
        Card.load_images()


    def reset(self):
        self.player_hand.reset()
        self.dealer_hand.reset()
        self.game_status = BlackJack.game_status_text[0]
        self.game_status_text_colors = BlackJack.game_status_text_colors[0]

        for _ in range(2):
            self.player_hand.add(self.cards_in_deck.deal())
            if self.cards_in_deck.size == 13:
                self.cards_in_deck.shuffle()
            self.dealer_hand.add(self.cards_in_deck.deal())
            if self.cards_in_deck.size == 13:
                self.cards_in_deck.shuffle()

        self._canvas.delete("all")
        self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
        self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
        self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
        self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
        self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
        self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
        self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))


    def player_hit(self):
        self.player_hand.add(self.cards_in_deck.deal())
        if self.cards_in_deck.size == 13:
            self.cards_in_deck.shuffle()

        if self.player_hand.total > 21:
            self.dealer_wins += 1
            self.game_status = BlackJack.game_status_text[2]
            self.game_status_text_colors = BlackJack.game_status_text_colors[1]

            self._canvas.delete("all")
            self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))
        else:
            self._canvas.delete("all")
            self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))


    def player_stand(self):
        while self.dealer_hand.total < 17:
            self.dealer_hand.add(self.cards_in_deck.deal())
            if self.cards_in_deck.size == 13:
                self.cards_in_deck.shuffle()
        
        if self.dealer_hand.total > 21 or self.dealer_hand.total < self.player_hand.total:
            self.player_wins += 1
            self.game_status = BlackJack.game_status_text[1]
            self.game_status_text_colors = BlackJack.game_status_text_colors[1]

            self._canvas.delete("all")
            self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))
        elif self.dealer_hand.total == self.player_hand.total:
            self.game_status = BlackJack.game_status_text[3]
            self.game_status_text_colors = BlackJack.game_status_text_colors[1]

            self._canvas.delete("all")
            self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))
        else:
            self.dealer_wins += 1
            self.game_status = BlackJack.game_status_text[2]
            self.game_status_text_colors = BlackJack.game_status_text_colors[1]

            self._canvas.delete("all")
            self._canvas.create_text(10, 10, anchor = "nw", text = f"Player Hand Total: {self.player_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.player_hand.draw(self._canvas, 10, 30, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 180, anchor = "nw", text = f"Dealer Hand Total: {self.dealer_hand.total}", font = ('Arial', 10, 'bold italic'))
            self.dealer_hand.draw(self._canvas, 10, 200, self._canvas_width, self._canvas_height)
            self._canvas.create_text(10, 350, anchor = "nw", text = f"Player Wins: {self.player_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(10, 370, anchor = "nw", text = f"Dealer Wins: {self.dealer_wins}", font = ('Arial', 10, 'bold italic'))
            self._canvas.create_text(250, 360, anchor = "nw", text = f"Game Status: {self.game_status}", fill = self.game_status_text_colors, font = ('Arial', 10, 'bold italic'))


def main():
    window = tk.Tk()
    window.title("Blackjack")
    game = BlackJack(window)
    window.mainloop()


if __name__ == "__main__":
    main()
