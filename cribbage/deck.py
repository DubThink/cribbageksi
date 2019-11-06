import random
from enum import Enum


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for i in range(1, 14):
                self.cards.append((i, suit))

    def shuffle(self):
        """
        shuffles the deck
        :return: None
        """
        random.shuffle(self.cards)

    def drawCard(self):
        """
        Draws a single card if possible. Throws an Exception if not
        :return: a card
        """
        if len(self.cards) < 1:
            raise Exception("Deck is out of cards")
        return self.cards.pop()

    def drawCards(self, count):
        """
        Draws count cards if possible. Throws and Exception if not
        :param count: the number of cards to draw
        :return: a list of cards
        """
        if len(self.cards) < count:
            raise Exception("Deck is out of cards")
        return [self.cards.pop() for i in range(count)]


if __name__ == "__main__":
    for i in range(10):
        deck=Deck()
        deck.shuffle()
        print(deck.cards)