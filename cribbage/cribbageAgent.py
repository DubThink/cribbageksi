import random
import heapq

class CribbageAgent:

    def discard_crib(self, hand, is_dealer):
        """
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
        pass

