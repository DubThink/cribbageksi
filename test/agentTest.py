from cribbage import cribbageAgent
import unittest

class TestAgent(unittest.TestCase):

    def test_is_pair(self):
        hand_example = [("s", 6), ("a", 6), ("k", 4), ("s", 4), ("c", 3), ("d", 3)]
        hand_example2 = [("s", 6), ("k", 4), ("a", 6), ("s", 4), ("c", 6), ("d", 6)]
        hand_example3 = [("a", 6), ("b", 4), ("c", 6), ("d", 6), ("e", 4), ("a", 5)]

        no_pair_example = [("s", 2), ("a", 3), ("d", 1), ("c", 4), ("e", 5), ("s", 6)]

        for


