from cribbage import cribbageAgent
import unittest


class TestAgent(unittest.TestCase):

    def test_random_discard_card(self):
        testAgent = cribbageAgent.CribbageAgent()

        hand1 = [(3, 2), (9, 1), (10, 4), (6, 1), (9, 2), (5, 1)]
        (discard1, discard2) = testAgent.discard_crib(hand1, True)
        passing = True
        if discard1 not in hand1:
            passing = False
        if discard2 not in hand1:
            passing = False
        assert passing
        








