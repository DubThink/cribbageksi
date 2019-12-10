import random
import heapq
from cribbage.deck import card_to_string, peg_val
from cribbage.scoreHand import expected_hand_value
from cribbage.deck import card_to_string
from copy import deepcopy
import cribbage.scoreHand as scorer
from itertools import combinations


class BaseCribbageAgent:

    def discard_crib(self, hand, is_dealer):
        """
        Discards two cards from a hand of 6
        :param hand: 6 cards
        :param is_dealer: if the player is the dealer, and will receive the crib
        :return: 2 cards to discard
        """
        raise NotImplementedError()



    def pegging_move(self, hand, sequence, current_sum):
        """
        Chooses a card to play during pegging
        :param hand: the player's hand
        :param sequence: the current sequence
        :param current_sum: the current sum on the table
        :return: a single Card
        """
        # Randomly choose a card that doesn't put sum over 31
        choices = []

        for card in hand:
            if peg_val(card) + current_sum <= 31:
                choices.append(card)
        choice = random.randint(0, len(choices) - 1)
        return choices[choice]


class RandomCribbageAgent(BaseCribbageAgent):

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


class GreedyCribbageAgent(BaseCribbageAgent):

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

            first_removed = hand[i]
            for j in range(i+1, len(hand)):
                copyhand = deepcopy(hand)
                second_removed = hand[j]
                copyhand.remove(first_removed)
                copyhand.remove(second_removed)

                for cut_card in possible_cut_cards:
                    if not i == j:
                        points = scorer.score_hand(copyhand, cut_card)
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
        # print("seq:", sequence)
        # print("hand: ", hand)
        # Check 4th card sequence
        # Any consecutive sequence of cards, play 4th sequence
        if len(sequence) > 3:
            cards = [peg_val(sequence[len(sequence) - 1]), peg_val(sequence[len(sequence) - 2]), peg_val(sequence[len(sequence) - 3])]
            cards.sort()
            if cards[0] + 1 in cards and cards[1] + 1 in cards:
                for i in hand:
                    if peg_val(i) == (cards[len(cards) - 1]) + 1 and peg_val(i) + current_sum <= 31:
                        return i

        # Check 3rd card sequence
        if len(sequence) > 2:
            cards = [peg_val(sequence[len(sequence) - 1]), peg_val(sequence[len(sequence) - 2])]
            cards.sort()
            if cards[0] + 1 in cards:
                for i in hand:
                    if peg_val(i) == cards[len(cards) - 1] + 1 and peg_val(i) + current_sum <= 31:
                        return i

        # Get sum to 15
        for i in hand:
            # print(i)
            if peg_val(i) + current_sum == 15:
                return i

        # Play same rank
        if len(sequence) > 0:
            check = sequence[len(sequence) - 1]
            for i in hand:
                if i == check and peg_val(i) + current_sum <= 31:
                    return i


        # Find a card to play that doesn't put sum over 31
        # Try to stop other player from getting sequence
        cards = []
        for i in hand:
            if peg_val(i) + current_sum <= 31:
                cards.append(i)
        if len(cards) > 0:
            return cards[0]
        #for card in cards:


def get_int_in_range(prompt,a,b):
    ret=None
    while ret is None:
        try:
            ret=int(input(prompt+"(%d-%d)>"%(a,b)))
        except ValueError:
            ret = None
            print("Invalid number")
            continue
        if a < ret < b:
            return ret
        ret = None
        print("Number not in range")


class AdvancedAgent(BaseCribbageAgent):

    def __init__(self):
        self.score = 0

    def discard_crib(self, hand, is_dealer):
        """

        :param hand:6 card hand dealt to player
        :param is_dealer: if the player is the dealer
        :param risk: -1 for risk averse, 0 for risk neutral, 1 for risk loving
        :return:
        """

        four_card_hands=self.get_possible_4_hands(hand)
        discarded=self.get_possible_discards(hand)
        hand_value_list=[]

        #creates a list of expected values for each 4 card hand
        for i in range(15):
            value=expected_hand_value(four_card_hands[i],discarded[i],-1)
            hand_value_list.append(value)

        #gets list of cards to discard corresponding to max value
        max_hand_value=0
        discard_index=0
        for i in range(15):
            if hand_value_list[i]>max_hand_value:
                max_hand_value=hand_value_list[i]
                discard_index=i
        cards_to_discard=discarded[discard_index]

        return cards_to_discard[0], cards_to_discard[1]




    def get_possible_4_hands(self, hand):
        possible_4 = []
        copyhand = deepcopy(hand)

        for i in range(len(copyhand)):
            first_card = copyhand[i]
            copyhand2 = deepcopy(copyhand)
            for j in range(i+1, len(copyhand2)):
                second_card = copyhand2[j]
                copyhand3 = deepcopy(copyhand2)
                copyhand3.remove(second_card)
                copyhand3.remove(first_card)
                possible_4.append(copyhand3)

        return possible_4

    def get_possible_discards(self, hand):
        possible_discards = []
        copyhand = deepcopy(hand)

        for i in range(len(copyhand)):
            first_card = copyhand[i]
            copyhand2 = deepcopy(copyhand)
            for j in range(i+1, len(copyhand2)):
                second_card = copyhand2[j]
                possible_discards.append((first_card, second_card))

        return possible_discards


class HumanAgent(BaseCribbageAgent):
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
