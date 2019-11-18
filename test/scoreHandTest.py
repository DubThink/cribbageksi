from cribbage.scoreHand import score_hand
import unittest


class TestScoreHand(unittest.TestCase):
    def test_no_points(self):
        hand=[(4,4),(3,1),(7,1),(12,2)]
        cut_card=(9,1)
        self.assertEqual(0, score_hand(hand,cut_card))

    def test_one_pair(self):
        hand = [(4, 4), (7, 1), (7, 1), (12, 2)]
        cut_card = (9, 1)
        self.assertEqual(2, score_hand(hand, cut_card))

    def test_two_pairs(self):
        hand = [(4, 4), (12, 1), (7, 1), (12, 2)]
        cut_card = (7, 1)
        self.assertEqual(4, score_hand(hand, cut_card))

    def test_3_of_a_kind(self):
        hand = [(4, 4), (4, 1), (4, 3), (12, 2)]
        cut_card = (6, 1)
        self.assertEqual(6, score_hand(hand, cut_card))

    def test_4_of_a_kind(self):
        hand = [(4, 4), (4, 1), (4, 3), (4, 2)]
        cut_card = (6, 1)
        self.assertEqual(12, score_hand(hand, cut_card))

    def test_right_jack(self):
        hand = [(2, 4), (11, 1), (8,3), (12, 2)]
        cut_card = (6, 1)
        self.assertEqual(1, score_hand(hand, cut_card))

    def test_4_card_flush(self):
        hand = [(1, 4), (9, 4), (12, 4), (3, 4)]
        cut_card = (8, 3)
        self.assertEqual(4, score_hand(hand, cut_card))

    def test_5_card_flush(self):
        hand = [(1, 4), (9, 4), (12, 4), (3, 4)]
        cut_card = (8, 4)
        self.assertEqual(5, score_hand(hand, cut_card))

    def test_run_of_3(self):
        hand = [(1, 4), (2, 1), (10, 3), (8, 2)]
        cut_card = (9, 2)
        self.assertEqual(3, score_hand(hand, cut_card))

    def test_run_of_4(self):
        hand = [(11, 4), (12, 1), (7, 3), (10, 2)]
        cut_card = (13, 2)
        self.assertEqual(4, score_hand(hand, cut_card))

    def test_run_of_5(self):
        hand = [(11, 4), (12, 1), (9, 3), (10, 2)]
        cut_card = (13, 2)
        self.assertEqual(5, score_hand(hand, cut_card))

    def test_one_fifteen(self):
        hand = [(5, 4), (4, 1), (7, 1), (1, 2)]
        cut_card = (8, 1)
        self.assertEqual(2, score_hand(hand, cut_card))

    def test_three_fifteens_and_pair(self):
        hand = [(5, 4), (7, 1), (7, 1), (12, 2)]
        cut_card = (8, 1)
        self.assertEqual(8, score_hand(hand, cut_card))

    def test_three_card_fifteen(self):
        hand = [(6, 4), (7, 1), (2, 1), (4, 2)]
        cut_card = (1, 1)
        self.assertEqual(2, score_hand(hand, cut_card))

    def test_four_card_fifteen(self):
        hand = [(6, 4), (3, 1), (2, 1), (4, 2)]
        cut_card = (1, 1)
        self.assertEqual(6, score_hand(hand, cut_card))

    def test_five_card_fifteen(self):
        hand = [(10, 4), (1, 1), (2, 1), (1, 2)]
        cut_card = (1, 3)
        self.assertEqual(8, score_hand(hand, cut_card))

    def test_double_run(self):
        hand = [(2, 4), (2, 1), (3, 1), (5, 2)]
        cut_card = (1, 3)
        self.assertEqual(8, score_hand(hand, cut_card))

    def test_good_hand(self):
        hand = [(10, 1), (11, 1), (11, 2), (12, 1)]
        cut_card = (5, 1)
        self.assertEqual(17, score_hand(hand, cut_card))

    def test_best_hand(self):
        hand = [(11, 1), (5, 2), (5, 3), (5, 4)]
        cut_card = (5, 1)
        self.assertEqual(29, score_hand(hand, cut_card))

if __name__ == '__main__':
    unittest.main()
