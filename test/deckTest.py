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
        s = set()
        deck = Deck()
        deck.shuffle()
        for i in range(52):
            v = deck.drawCard()
            self.assertFalse(v in s)
            s.add(v)
        self.assertTrue(len(deck.cards)==0)

    def test_draw(self):
        s = set()
        deck = Deck()
        deck.shuffle()
        for i in [5,9,2,1,0,13,10,2,6,4]:
            v = deck.drawCards(i)
            ss = set(v)
            self.assertTrue(len(ss) == len(v))
            self.assertTrue(s.isdisjoint(ss))
            s = s.union(s)
        self.assertTrue(len(deck.cards) == 0)


if __name__ == '__main__':
    unittest.main()