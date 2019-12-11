from cribbage.deck import *

import unittest
from cribbage.Agents import BaseCribbageAgent
from cribbage.cribbageGame import CribbageGame, IllegalMoveException


class TestAgent(BaseCribbageAgent):
    def __init__(self,discard_func=None,pegging_func=None):
        self.discard_func=discard_func
        self.pegging_func=pegging_func

    def discard_crib(self, hand, is_dealer):
        if self.discard_func is not None:
            return self.discard_func(hand,is_dealer)
        else:
            return BaseCribbageAgent.discard_crib(self, hand, is_dealer)

    def pegging_move(self, hand, sequence, current_sum):
        if self.pegging_func is not  None:
            return self.pegging_func(hand, sequence, current_sum)
        else:
            BaseCribbageAgent.pegging_move(self, hand, sequence, current_sum)


class TestGame(unittest.TestCase):

    def test_pegging_limit31(self):
        # agent that always tries to play cards
        game = CribbageGame(TestAgent(pegging_func=(lambda h,s,c : h[0] if h else None)), TestAgent(pegging_func=(lambda h,s,c : h[0] if h else None)))
        hand_a = [(10,DIAMONDS), (11,CLUBS), (11,HEARTS),]
        hand_b = [(10,SPADES), (11,DIAMONDS), (11,SPADES),]
        self.assertRaises(IllegalMoveException, game.pegging, hand_a, hand_b, True)
        hand_a = [(2, DIAMONDS), (3, CLUBS), (5, HEARTS),(8,SPADES)]
        hand_b = [(3, SPADES), (4, DIAMONDS), (5, SPADES),(1,DIAMONDS)]
        # make sure it runs fine with numbers adding to 31
        game.pegging(hand_a,hand_b,True)
        # self.assertTrue(len(deck.cards)==52)

    def test_pegging_notplaying(self):
        game = CribbageGame(TestAgent(pegging_func=(lambda h,s,c : None)), TestAgent(pegging_func=(lambda h,s,c : h[0])))
        hand_a = [(2, DIAMONDS), (3, CLUBS), (5, HEARTS),(8,SPADES)]
        hand_b = [(3, SPADES), (4, DIAMONDS), (5, SPADES),(1,DIAMONDS)]
        self.assertRaises(IllegalMoveException, game.pegging, hand_a, hand_b, True)
        # self.assertTrue(len(deck.cards)==52)


if __name__ == '__main__':
    unittest.main()
