from cribbage import cribbageAgent
import unittest


class TestAgent(unittest.TestCase):

    def test_random_discard_card(self):
        testAgent = cribbageAgent.CribbageAgent()

        hand1 = [(3, 2), (9, 1), (10, 4), (6, 1), (9, 2), (5, 1)]
        (discard1, discard2) = testAgent.discard_crib(hand1)
        assert discard1 < len(hand1)
        assert discard1 >= 0
        assert discard2 < len(hand1)
        assert discard2 >= 0







