import random
import heapq
from cribbage.deck import card_to_string
from copy import deepcopy
import cribbage.scoreHand as scorer


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

    def find_pair(self, hand):
        """
        Thy
        Looks through hand, finds possible pairs
        :param hand: a list of tuples, each tuple contains the suit of the card and the value of the card
        :return: a set of pairs of cards, ordered next to one another
        """
        paired = []
        for current in range(0, len(hand), 1):
            current_card = hand[current]
            (current_value, current_suit) = current_card
            for compare in range(current + 1, len(hand), 1):
                compare_card = hand[compare]
                (compare_value, compare_suit) = compare_card
                if compare_value == current_value:
                    paired.append(current_card)
                    paired.append(compare_card)
                    break

        return paired

    def discard_two(self, hand, index1, index2):
        """
        Thy
        Takes a 6-card hand, removes cards at index1 and index2
        :param hand: 6-card hand which is a list of tuples, each tuple (1 card) contains the value and the suit of the card
        :param index1: index of the first card to remove
        :param index2: index of the second card to remove
        :return: a 4-card hand without the removed cards,
                 a 6-card hand IF EITHER of the indices is out of range
        """
        if index1 >= len(hand) or index2 >= len(hand):
            return hand

        else:
            hand.remove(hand[index1])
            hand.remove(hand[index2])
            return hand

    def what_if(self, hand):
        """
        Thy
        Generates a priority queue based on 4-card hand scores with different permutations of 2 discarded cards
        :param hand: 6-card hand
        :return: a priority queue of 4-card hand based on their scores
        """
        priorityq = []
        possible_cut_cards = [(1, 1), (1, 2), (1, 3), (1, 4),
                              (2, 1), (2, 2), (2, 3), (2, 4),
                              (3, 1), (3, 2), (3, 3), (3, 4),
                              (4, 1), (4, 2), (4, 3), (4, 4),
                              (5, 1), (5, 2), (5, 3), (5, 4),
                              (6, 1), (6, 2), (6, 3), (6, 4),
                              (7, 1), (7, 2), (7, 3), (7, 4),
                              (8, 1), (8, 2), (8, 3), (8, 4),
                              (9, 1), (9, 2), (9, 3), (9, 4),
                              (10, 1), (10, 2), (10, 3), (10, 4),
                              (11, 1), (11, 2), (11, 3), (11, 4),
                              (12, 1), (12, 2), (12, 3), (12, 4),
                              (13, 1), (13, 2), (13, 3), (13, 4)]
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
                    heapq.heappush(priorityq, (points, copyhand2))

        return priorityq

    def pegging_move(self, hand, sequence, current_sum):
        """
        Chooses a card to play during pegging
        :param hand: the player's hand
        :param sequence: the current sequence
        :param current_sum: the current sum on the table
        :return: a single Card
        """
        # print("seq:", sequence)
        # print("hand: ", hand)
        # Get sum to 15
        for i in hand:
            #print(i)
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


class HumanAgent():
    def discard_crib(self, hand, is_dealer):
        print("You are the dealer" if is_dealer else "You are not the dealer")
        print("hand: ",", ".join([card_to_string(c) for c in hand]))
        n1 = int(input("discard 1-6 >"))
        n2 = int(input("discard 1-6 >"))
        return [hand[n1-1],hand[n2-1]]

    def pegging_move(self, hand, sequence, current_sum):
        print("hand: ",", ".join([card_to_string(c) for c in hand]))
        n1 = int(input("play 1-%d >"%len(hand)))
        return hand[n1-1]
