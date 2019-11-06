from cribbage.deck import Deck, Suit

import unittest

class TestDeck(unittest.TestCase):

    def test_shuffle(self):
        deck=Deck()
        deck.shuffle()
        self.assertTrue(len(deck.cards)==52)
        for i in range(1,14):
            for suit in Suit:
                self.assertTrue((i,suit) in  deck.cards)


    def test_draw(self):
        pass

if __name__ == '__main__':
    unittest.main()