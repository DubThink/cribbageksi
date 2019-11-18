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

    #
    # def score_hand(hand4cards, cutcard):
    # """
    # Returns the point value of a 4 card hand with the given cut card
    # :param hand4cards: the 4 cards in the player's hand
    # :param cutcard: cut card
    # :return: integer point value of the hand
    # """
    #     points = 0
    #     # right jack
    #     for card in hand4cards:
    #         if card[0] == 11 and cutcard[1] == card[1]:  # if card in hand is a Jack and its suit matches the cut card
    #             points += 1
    #     # flushes
    #     if hand4cards[0][1] == hand4cards[1][1] == hand4cards[2][1] == hand4cards[3][1]:
    #         points += 4
    #         if hand4cards[0][1] == cutcard[1]:
    #             points += 1
    #     # create list of sorted 5 card hand
    #     hand_queue = []
    #     hand4cards.append(cutcard)
    #     for i in range(5):
    #         heapq.heappush(hand_queue, hand4cards[i])
    #     sorted5cards = heapq.nsmallest(5, hand_queue)
    #
    #
    #     # 15's
    #     start_card_index = 0
    #     while start_card_index < 4:
    #         index = start_card_index + 1
    #         for i in range(index, 5):
    #             value1 = sorted5cards[start_card_index][0]
    #             if value1 in range(11,14):
    #                 value1 = 10
    #             value2 = sorted5cards[i][0]
    #             if value2 in range(11,14):
    #                 value2 = 10
    #             if value1 + value2 == 15:
    #                 points += 2
    #         start_card_index += 1
    #
    #
    #     #pairs 15's
    #     index_combinations2 = combinations([0,1,2,3,4], 2)
    #     for combination in list(index_combinations2):
    #         value1 = sorted5cards[combination[0]][0]
    #         if value1 in range(11, 14):
    #             value1 = 10
    #         value2 = sorted5cards[combination[1]][0]
    #         if value2 in range(11, 14):
    #             value2 = 10
    #         if value1 + value2 == 15:
    #             points += 2
    #
    #     #3 card 15's
    #     index_combinations3 = combinations([0, 1, 2, 3, 4], 3)
    #     for combination in list(index_combinations3):
    #         value1 = sorted5cards[combination[0]][0]
    #         if value1 in range(11, 14):
    #             value1 = 10
    #         value2 = sorted5cards[combination[1]][0]
    #         if value2 in range(11, 14):
    #             value2 = 10
    #         value3 = sorted5cards[combination[2]][0]
    #         if value3 in range(11, 14):
    #             value3 = 10
    #         if value1 + value2 + value3 == 15:
    #             points += 2
    #
    #     # 4 card 15's
    #     index_combinations4 = combinations([0, 1, 2, 3, 4], 4)
    #     for combination in list(index_combinations4):
    #         value1 = sorted5cards[combination[0]][0]
    #         if value1 in range(11, 14):
    #             value1 = 10
    #         value2 = sorted5cards[combination[1]][0]
    #         if value2 in range(11, 14):
    #             value2 = 10
    #         value3 = sorted5cards[combination[2]][0]
    #         if value3 in range(11, 14):
    #             value3 = 10
    #         value4 = sorted5cards[combination[3]][0]
    #         if value4 in range(11, 14):
    #             value4 = 10
    #         if value1 + value2 + value3 + value4 == 15:
    #             points += 2
    #
    #     # 5 card 15's
    #     sum=0
    #     for i in range(5):
    #         sum+=sorted5cards[i][0]
    #     if sum==15:
    #         points+=2
    #
    #     # runs
    #     if sorted5cards[0][0] == sorted5cards[1][0] - 1 == sorted5cards[2][0] - 2:
    #         points += 3
    #         if sorted5cards[2][0] == sorted5cards[3][0] - 1:
    #             points += 1
    #             if sorted5cards[3][0] == sorted5cards[4][0] - 1:
    #                 points += 1
    #     elif sorted5cards[1][0] == sorted5cards[2][0] - 1 == sorted5cards[3][0] - 2:
    #         points += 3
    #         if sorted5cards[3][0] == sorted5cards[4][0] - 1:
    #             points += 1
    #     elif sorted5cards[2][0] == sorted5cards[3][0] - 1 == sorted5cards[4][0] - 2:
    #         points += 3
    #     for start_index in range(3):
    #         next_index=start_index+1
    #         consecutive_cards_count = 1
    #         duplicates_count = 0
    #         while next_index<5:
    #             if sorted5cards[start_index][0] == sorted5cards[next_index][0]:
    #                 duplicates_count += 1
    #             elif sorted5cards[start_index][0] == sorted5cards[next_index][0] - 1:
    #                 consecutive_cards_count += 1
    #             else:
    #                 break
    #             start_index = next_index
    #             next_index += 1
    #         multiplier = 1
    #         if duplicates_count > 0:
    #             multiplier = duplicates_count+1
    #         if consecutive_cards_count >= 3:
    #             points += multiplier * consecutive_cards_count
    #             break
    #
    #     # pairs/3 of a kind/4 of a kind
    #     start_card_index = 0
    #


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
