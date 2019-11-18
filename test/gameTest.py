from cribbage.deck import Deck, Suit

import unittest
from cribbage.Agents import CribbageAgent
from cribbage.cribbageGame import CribbageGame, IllegalMoveException


class TestAgent(CribbageAgent):
    def __init__(self,discard_func=None,pegging_func=None):
        self.discard_func=discard_func
        self.pegging_func=pegging_func

    def discard_crib(self, hand, is_dealer):
        if self.discard_func is not None:
            return self.discard_func(hand,is_dealer)
        else:
            return CribbageAgent.discard_crib(self, hand, is_dealer)

    def pegging_move(self, hand, sequence, current_sum):
        if self.pegging_func is not  None:
            return self.pegging_func(hand, sequence, current_sum)
        else:
            CribbageAgent.pegging_move(self, hand, sequence, current_sum)


class TestGame(unittest.TestCase):

    def test_pegging_limit31(self):
        # agent that always tries to play cards
        game = CribbageGame(TestAgent(pegging_func=(lambda h,s,c : h[0])), TestAgent(pegging_func=(lambda h,s,c : h[0])))
        hand_a = [(10,Suit.DIAMONDS), (11,Suit.CLUBS), (11,Suit.HEARTS),]
        hand_b = [(10,Suit.SPADES), (11,Suit.DIAMONDS), (11,Suit.SPADES),]
        self.assertRaises(IllegalMoveException, game.pegging, hand_a, hand_b, True)
        hand_a = [(2, Suit.DIAMONDS), (3, Suit.CLUBS), (5, Suit.HEARTS),(8,Suit.SPADES)]
        hand_b = [(3, Suit.SPADES), (4, Suit.DIAMONDS), (5, Suit.SPADES),(1,Suit.DIAMONDS)]
        # make sure it runs fine with numbers adding to 31
        game.pegging(hand_a,hand_b,True)
        # self.assertTrue(len(deck.cards)==52)

    def test_pegging_notplaying(self):
        game = CribbageGame(TestAgent(pegging_func=(lambda h,s,c : None)), TestAgent(pegging_func=(lambda h,s,c : h[0])))
        hand_a = [(2, Suit.DIAMONDS), (3, Suit.CLUBS), (5, Suit.HEARTS),(8,Suit.SPADES)]
        hand_b = [(3, Suit.SPADES), (4, Suit.DIAMONDS), (5, Suit.SPADES),(1,Suit.DIAMONDS)]
        self.assertRaises(IllegalMoveException, game.pegging, hand_a, hand_b, True)
        # self.assertTrue(len(deck.cards)==52)

if __name__ == '__main__':
    unittest.main()