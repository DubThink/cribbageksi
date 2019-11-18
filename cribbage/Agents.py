import random
import heapq
from cribbage.deck import card_to_string
from cribbage.deck import card_to_string
from copy import deepcopy
import cribbage.scoreHand as scorer
from itertools import combinations

class RandomCribbageAgent:

    def __init__(self):
        self.score = 0

    def discard_crib(self, hand, is_dealer):
        """
        Thy
        Discards two cards from a hand of 6
        :param hand: 6 cards
        :param is_dealer: if the player is the dealer, and will receive the crib
        :return: 2 cards to discard
        """
        # if I am dealer, I get the crib
        if is_dealer:
            end = len(hand)
            discard_index = random.randint(0, end-1)
            discard_index2 = random.randint(0, end-2)
            if discard_index == discard_index2:
                discard_index2 += 1
            return hand[discard_index], hand[discard_index2]

        else:
            end = len(hand)
            discard_index = random.randint(0, end-1)
            discard_index2 = random.randint(0, end-2)
            if discard_index == discard_index2:
                discard_index2 += 1
            return hand[discard_index], hand[discard_index2]


class GreedyCribbageAgent:

    def __init__(self):
        self.score = 0

    def discard_crib(self, hand, is_dealer):
        """
        Thy
        :param hand: list of 6 cards, each card is a tuple of value and suit
        :param is_dealer: whether the player is the dealer
        :return: the tuple of 2 cards to discard
        """
        possible_choices = self.bfs(hand)
        highest_score_hand = possible_choices[0]
        (points, first_index, second_index) = highest_score_hand
        return hand[first_index], hand[second_index]

    def bfs(self, hand):
        """
        Thy
        Generates a priority queue based on 4-card hand scores with different permutations of 2 discarded cards
        :param hand: 6-card hand
        :return: a priority queue of 4-card hand based on their scores
        """
        priorityq = []
        possible_cut_cards = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)]
        for i in range(len(hand)):
            copyhand = deepcopy(hand)

            first_removed = copyhand[i]
            copyhand.remove(first_removed)
            for j in range(i, len(copyhand)):
                copyhand2 = deepcopy(copyhand)
                second_removed = copyhand[j]
                copyhand2.remove(second_removed)

                for cut_card in possible_cut_cards:
                    points = scorer.score_hand(copyhand2, cut_card)
                    heapq.heappush(priorityq, (-points, i, j))

        return priorityq

    def pegging_move(self, hand, sequence, current_sum):
        """
        Chooses a card to play during pegging
        :param hand: the player's hand
        :param sequence: the current sequence
        :param current_sum: the current sum on the table
        :return: a single Card
        """
        print("seq:", sequence)
        print("hand: ", hand)
        # Check 4th card sequence
        # Any consecutive sequence of cards, play 4th sequence
        if len(sequence) > 3:
            cards = [sequence[len(sequence) - 1][0], sequence[len(sequence) - 2][0], sequence[len(sequence) - 3][0]]
            cards.sort()
            if cards[0] + 1 in cards and cards[1] + 1 in cards:
                for i in hand:
                    if i[0] == cards[len(cards) - 1] + 1:
                        return i

        # Check 3rd card sequence
        if len(sequence) > 2:
            cards = [sequence[len(sequence) - 1][0], sequence[len(sequence) - 2][0]]
            cards.sort()
            if cards[0] + 1 in cards:
                for i in hand:
                    if i[0] == cards[len(cards) - 1] + 1:
                        return i

        # Get sum to 15
        for i in hand:
            # print(i)
            if i[0] + current_sum == 15:
                return i

        # Play same rank
        if len(sequence) > 0:
            check = sequence[len(sequence) - 1]
            for i in hand:
                if i == check:
                    return i

        # Find a card to play that doesn't put sum over 31
        for i in hand:
            if i[0] + current_sum <= 31:
                return i


class HumanAgent(CribbageAgent):
    def discard_crib(self, hand, is_dealer):
        print("You are the dealer" if is_dealer else "You are not the dealer")
        print("hand: ",", ".join([card_to_string(c) for c in hand]))
        n1 = get_int_in_range("discard card A", 1, 6)
        while True:
            n2 = get_int_in_range("discard card B", 1, 6)
            if n1 != n2:
                break
            print("Cannot discard the same card twice.")
        return [hand[n1-1], hand[n2-1]]

    def pegging_move(self, hand, sequence, current_sum):
        print("hand: ",", ".join([card_to_string(c) for c in hand]))
        n1 = get_int_in_range("play card ", 1, len(hand))

        return hand[n1-1]
