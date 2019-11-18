from cribbage import Agents
import unittest

hand1 = [(3, 2), (9, 1), (10, 4), (6, 1), (9, 2), (5, 1)]

randomTestAgent = Agents.RandomCribbageAgent()
greedyTestAgent = Agents.GreedyCribbageAgent()


class RandomAgentTest(unittest.TestCase):

    def test_random_discard_card(self):
        (discard1, discard2) = randomTestAgent.discard_crib(hand1, True)
        passing = True
        if discard1 not in hand1:
            passing = False
        if discard2 not in hand1:
            passing = False
        assert passing


class GreedyAgentTest(unittest.TestCase):

    def test_bfs(self):
        possible_discards = greedyTestAgent.bfs(hand1)
        assert not len(possible_discards) == 0

    def test_discard_crib(self):
        (discard1, discard2) = greedyTestAgent.discard_crib(hand1, True)
        passing = True
        if discard1 not in hand1:
            passing = False
        if discard2 not in hand1:
            passing = False
        assert passing





