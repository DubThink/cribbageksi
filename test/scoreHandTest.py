from cribbage.scoreHand import score_hand,pairs,two_card_fifteens,three_card_fifteens,four_card_fifteens,five_card_fifteens,runs,right_jack,flush,sort_cards
import unittest

class TestScoreHand(unittest.TestCase):

    def test_right_jack(self):
        #right jack
        hand = [(10, 1), (11, 1), (1, 2), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(1, right_jack(hand,cutcard))


    def test_not_right_jack(self):
        hand = [(10, 2), (11, 3), (1, 2), (5, 0)]
        cutcard = (5, 1)
        self.assertEqual(0, right_jack(hand,cutcard))

    def test_four_card_flush(self):
        #jack in hand but not matching suit
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 2)
        self.assertEqual(0, right_jack(hand, cutcard))

        #no jack in hand
        hand = [(10, 1), (4, 1), (1, 1), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(0, right_jack(hand, cutcard))

    def test_crib_flush(self):
        #4 card flush
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 3)
        self.assertEqual(0, flush(hand, cutcard, True))

        #5 card flush
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(5, flush(hand, cutcard, True))

    def test_flush(self):
        #4 card flush
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 3)
        self.assertEqual(4, flush(hand,cutcard,False))

        #5 card flush
        hand = [(10, 1), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(5, flush(hand, cutcard,False))

        #no flush
        hand = [(10, 2), (11, 1), (1, 1), (3, 1)]
        cutcard = (5, 1)
        self.assertEqual(0, flush(hand, cutcard, False))

    def test_not_flush(self):
        hand = [(10, 1), (11, 1), (1, 1), (3, 2)]
        cutcard = (5, 1)
        self.assertEqual(0, flush(hand,cutcard, False))

    def test_pairs(self):

        #one pair
        hand = [(12, 1), (7, 4), (8, 2), (12, 3)]
        cutcard = (4, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, pairs(sorted5cards))

        #3 of a kind
        hand = [(12, 1), (12, 4), (8, 2), (12, 3)]
        cutcard = (11, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(6, pairs(sorted5cards))

        #4 of a kind
        hand = [(8, 1), (8, 4), (8, 2), (8, 3)]
        cutcard = (11, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(12, pairs(sorted5cards))

        #2 pairs
        hand = [(12, 1), (11, 4), (8, 2), (12, 3)]
        cutcard = (11, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(4, pairs(sorted5cards))

        #3 of a kind and a pair
        hand = [(12, 1), (11, 4), (11, 2), (12, 3)]
        cutcard = (11, 1)
        sorted5cards=sort_cards(hand,cutcard)
        self.assertEqual(8, pairs(sorted5cards))

        #no pairs
        hand = [(12, 1), (11, 4), (8, 2), (10, 3)]
        cutcard = (3, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, pairs(sorted5cards))

    def test_runs(self):

        #run of 3 with two duplicates
        hand = [(10, 1), (11, 1), (11, 2), (12, 1)]
        cutcard = (10, 3)
        sorted5cards=sort_cards(hand,cutcard)
        self.assertEqual(12, runs(sorted5cards))

        #double run of 3
        hand = [(10, 1), (11, 1), (4, 2), (12, 1)]
        cutcard = (10, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(6, runs(sorted5cards))

        # double run of 4
        hand = [(1, 1), (2, 1), (3, 2), (2, 1)]
        cutcard = (4, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(8, runs(sorted5cards))

        #run of 3
        hand = [(1, 1), (2, 1), (3, 2), (12, 1)]
        cutcard = (10, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(3, runs(sorted5cards))

        # run of 4
        hand = [(1, 1), (2, 1), (3, 2), (12, 1)]
        cutcard = (4, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(4, runs(sorted5cards))

        #run of 5
        hand = [(1, 1), (2, 1), (4, 2), (5, 1)]
        cutcard = (3, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(5, runs(sorted5cards))

        #no runs
        hand = [(1, 1), (3, 1), (11, 2), (5, 1)]
        cutcard = (10, 3)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, runs(sorted5cards))

    def test_two_card_fifteens(self):

        # 1 two-card 15
        hand = [(2, 1), (11, 1), (7, 2), (3, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, two_card_fifteens(sorted5cards))

        #3 two-card 15's
        hand = [(10, 1), (11, 1), (7, 2), (8, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(6, two_card_fifteens(sorted5cards))

        #no two-card 15's
        hand = [(10, 1), (11, 1), (7, 2), (7, 1)]
        cutcard = (3, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, two_card_fifteens(sorted5cards))


    def test_three_card_fifteens(self):
        #1 three-card 15
        hand = [(4, 1), (10, 1), (1, 2), (8, 1)]
        cutcard = (2, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, three_card_fifteens(sorted5cards))

        #2 three-card 15's
        hand = [(4, 1), (3, 1), (4, 2), (8, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(4, three_card_fifteens(sorted5cards))

        # no three-card 15's
        hand = [(4, 1), (3, 1), (4, 2), (1, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, three_card_fifteens(sorted5cards))

    def test_four_card_fifteens(self):
        #1 four-card 15
        hand = [(10, 1), (1, 1), (1, 2), (3, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, four_card_fifteens(sorted5cards))

        # no four-card 15's
        hand = [(1, 1), (3, 1), (4, 2), (1, 1)]
        cutcard = (5, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, four_card_fifteens(sorted5cards))


    def test_five_card_fifteens(self):
        #1 five-card 15
        hand = [(10, 1), (1, 1), (1, 2), (2, 1)]
        cutcard = (1, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(2, five_card_fifteens(sorted5cards))

        # no five-card 15's
        hand = [(10, 1), (8, 1), (1, 2), (2, 1)]
        cutcard = (1, 1)
        sorted5cards = sort_cards(hand, cutcard)
        self.assertEqual(0, five_card_fifteens(sorted5cards))

    def test_no_points(self):
        hand = [(4, 0), (3, 1), (7, 1), (12, 2)]
        cutcard = (9, 1)
        self.assertEqual(0,score_hand(hand,cutcard,False))

    def test_best_hand(self):
        hand = [(11, 1), (5, 2), (5, 3), (5, 0)]
        cutcard = (5, 1)
        self.assertEqual(29, score_hand(hand, cutcard,False))

    def test_it_broke(self):
        hand = [(4,1),(5,2),(7,3),(11,3)]
        cutcard = (11,2)
        self.assertEqual(6,score_hand(hand,cutcard,False))



if __name__ == '__main__':
    unittest.main()
