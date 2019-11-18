import random
import heapq
from cribbage.deck import card_to_string, peg_val


class CribbageAgent:

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

    def is_pair(self, hand):
        """
        Thy
        Looks through hand, finds possible pairs
        :param hand: a list of tuples, each tuple contains the suit of the card and the value of the card
        :return: a set of pairs of cards, ordered next to one another
        """
        paired = []
        for current in range(0, len(hand), 1):
            current_card = hand[current]
            (current_suit, current_value) = current_card
            for compare in range(current + 1, len(hand), 1):
                compare_card = hand[compare]
                (compare_suit, compare_value) = compare_card
                if compare_value == current_value:
                    paired.append(current_card)
                    paired.append(compare_card)
                    break

        return paired

    def is_pair_royal(self, hand):
        royal = []
        for current in range(len(hand)):
            current_card = hand[current]
            (current_suit, current_value) = current_card
            royal.append(current_card)
            for compare in range(current + 1, len(hand), 1):
                compare_card = hand[compare]
                (compare_suit, compare_value) = compare_card
                if compare_value == current_value and compare_card not in royal:
                    royal.append(compare_card)

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
            if peg_val(i) + current_sum == 15:
                return i

        # Play same rank
        if len(sequence) > 0:
            check = sequence[len(sequence) - 1]
            for i in hand:
                if i == check:
                    return i

        # Find a card to play that doesn't put sum over 31
        for i in hand:
            if peg_val(i) + current_sum <= 31:
                return i


def get_int_in_range(prompt, a, b):
    while True:
        try:
            n = int(input(prompt+" %d-%d>" % (a, b)))
        except ValueError:
            print("Invalid number.")
            continue
        if a <= n <= b:
            return n
        print("Number not in range")


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
