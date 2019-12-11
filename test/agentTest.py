from cribbage import Agents
import unittest

hand1 = [(3, 2), (9, 1), (10, 4), (6, 1), (9, 2), (5, 1)]

randomTestAgent = Agents.RandomCribbageAgent()
greedyTestAgent = Agents.GreedyCribbageAgent()
advancedTestAgent = Agents.AdvancedAgent()


class RandomAgentTest(unittest.TestCase):

    def test_random_discard_card(self):
        """
        Thy
        :return: tests random agent's discarding function
        """
        (discard1, discard2) = randomTestAgent.discard_crib(hand1, True)
        passing = True
        if discard1 not in hand1:
            passing = False
        if discard2 not in hand1:
            passing = False
        assert passing


class GreedyAgentTest(unittest.TestCase):

    def test_discard_crib(self):
        """
        Thy
        :return: tests greedy agent's discarding function
        """
        (discard1, discard2) = greedyTestAgent.discard_crib(hand1, True)
        passing = True
        if discard1 not in hand1:
            passing = False
        if discard2 not in hand1:
            passing = False
        assert passing

    def test_bfs(self):
        """
        Thy
        :return: tests greedy agent's breadth first search function
        """
        passing = False
        returned_q = greedyTestAgent.bfs(hand1)
        print(returned_q)
        first_choice = returned_q[0]
        (points, index1, index2) = first_choice
        if index1 in range(len(hand1)) and index2 in range(len(hand1)):
            passing = True
        if points <= 0:
            passing = True
        assert passing

class AdvancedAgentTest(unittest.TestCase):

    """
    Thy
    """
    def test_get_possible_4_hands(self):
        possible_4 = advancedTestAgent.get_possible_4_hands(hand1)
        passing = True
        if len(possible_4) == 0:
            passing = False
        random_card = (8, 1)
        if random_card in possible_4:
            passing = False
        assert passing

    def test_get_possible_discards(self):
        possible_discards = advancedTestAgent.get_possible_discards(hand1)
        passing = True
        if len(possible_discards) == 0:
            passing = False

        hand2 = []
        possible_discards2 = advancedTestAgent.get_possible_discards(hand2)
        if not len(possible_discards2) == 0:
            passing = False
        assert passing


if __name__ == '__main__':
    unittest.main()
