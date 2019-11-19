from cribbage.scoreHand import score_hand,pairs,two_card_fifteens,three_card_fifteens,four_card_fifteens,five_card_fifteens,runs,right_jack,flush,sort_cards
import unittest

class TestScoreHand(unittest.TestCase):

    def test_right_jack(self):
        hand = [(10, 1), (11, 1), (1, 2), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(1, right_jack(hand,cutcard))

    def test_not_right_jack(self):
        hand = [(10, 2), (11, 3), (1, 2), (5, 0)]
        cutcard = (5, 1)
        self.assertEqual(0, right_jack(hand,cutcard))

    def test_four_card_flush(self):
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 3)
        self.assertEqual(4, flush(hand,cutcard))

    def test_five_card_flush(self):
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(5, flush(hand,cutcard))

    def test_not_flush(self):
        hand = [(10, 1), (11, 1), (1, 1), (3, 2)]
        cutcard = (5, 1)
        self.assertEqual(0, flush(hand,cutcard))

    def test_pairs(self):
        hand = [(12, 1), (11, 0), (11, 2), (12, 3)]
        cutcard = (11, 1)
        sorted5cards=sort_cards(hand,cutcard)
        self.assertEqual(8,pairs(sorted5cards))

    def test_runs(self):
        hand = [(10, 1), (11, 1), (11, 2), (12, 1)]
        cutcard = (5, 1)
        sorted5cards=sort_cards(hand,cutcard)
        self.assertEqual(6,runs(sorted5cards))

    def test_two_card_fifteens(self):
        hand = [(10, 1), (11, 1), (7, 2), (8, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(6, two_card_fifteens(sorted5cards))

    def test_three_card_fifteens(self):
        hand = [(4, 1), (3, 1), (4, 2), (8, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(4, three_card_fifteens(sorted5cards))

    def test_four_card_fifteens(self):
        hand = [(10, 1), (1, 1), (1, 2), (3, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, four_card_fifteens(sorted5cards))

    def test_five_card_fifteens(self):
        hand = [(10, 1), (1, 1), (1, 2), (2, 1)]
        cutcard = (1, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, five_card_fifteens(sorted5cards))

    def test_no_points(self):
        hand = [(4, 0), (3, 1), (7, 1), (12, 2)]
        cutcard = (9, 1)
        self.assertEqual(0,score_hand(hand,cutcard))

    def test_best_hand(self):
        hand = [(11, 1), (5, 2), (5, 3), (5, 0)]
        cutcard = (5, 1)
        self.assertEqual(29, score_hand(hand, cutcard))



if __name__ == '__main__':
    unittest.main()
