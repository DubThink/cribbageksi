import random
import heapq
from cribbage.deck import card_to_string, peg_val
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
        raise NotImplementedError()


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

        if not hand:
            return None

        for card in hand:
            if peg_val(card) + current_sum <= 31:
                choices.append(card)

        if not choices:
            return None

        choice = random.randint(0, len(choices) - 1)
        return choices[choice]


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

    def discard_crib(self, hand, is_dealer):
        """

        :param hand:
        :param is_dealer:
        :return:
        """
        pass

    def bfs(self, hand):
        possible_4 = []
        getrid = []
        copyhand = deepcopy(hand)

        for i in range(len(copyhand)):
            first_card = copyhand[i]
            copyhand2 = deepcopy(copyhand)
            for j in range(i, len(copyhand2)):
                second_card = copyhand2[j]
                copyhand2.remove(second_card)
                getrid.append((first_card, second_card))
                possible_4.append(copyhand2)
            copyhand.remove(first_card)

        return possible_4


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
