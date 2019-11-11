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

    def is_pair(self, hand):
        """
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

    def pegging_move(self, hand, sequence, current_sum):
        """
        Chooses a card to play during pegging
        :param hand: the player's hand
        :param sequence: the current sequence
        :param current_sum: the current sum on the table
        :return: a single Card
        """
        pass

    def score_hand(self, hand4cards, cutcard):
        """
        Returns the point value of a 4 card hand with the given cut card
        :param hand4cards: the 4 cards in the player's hand
        :param cutcard: cut card
        :return: integer point value of the hand
        """

        points = 0

        # create list of sorted 5 card hand

        hand_queue = []
        hand4cards.append(cutcard)
        for i in range(5):
            heapq.heappush(hand_queue, hand4cards[i])
        sorted5cards = heapq.nlargest(5, hand_queue)

        # right jack
        for card in sorted5cards:
            if card[1] == 11 and cutcard[2] == card[2]:  # if card in hand is a Jack and its suit matches the cut card
                points += 1

        # flushes
        if hand4cards[0][1] == hand4cards[1][1] == hand4cards[2][1] == hand4cards[3][1] == hand4cards[4][1]:
            points += 4
            if hand4cards[0][1] == cutcard[1]:
                points += 1

        # 15's
        start_card_index = 0
        while start_card_index < 4:
            index = start_card_index + 1
            for i in range(index, 5):
                if sorted5cards[start_card_index][0] + sorted5cards[i][0] == 15:
                    points += 2
            start_card_index += 1

        # runs
        if sorted5cards[0][0] == sorted5cards[1][0] - 1 == sorted5cards[2][0] - 2:
            points += 3
            if sorted5cards[2][0] == sorted5cards[3][0] - 1:
                points += 1
                if sorted5cards[3][0] == sorted5cards[4][0] - 1:
                    points += 1
        elif sorted5cards[1][0] == sorted5cards[2][0] - 1 == sorted5cards[3][0] - 2:
            points += 3
            if sorted5cards[3][0] == sorted5cards[4][0] - 1:
                points += 1
        elif sorted5cards[2][0] == sorted5cards[3][0] - 1 == sorted5cards[4][0] - 2:
            points += 3

        # pairs/3 of a kind/4 of a kind
        currentIndex = 0
        while currentIndex < 4:
            addToIndex = 0
            if currentIndex == 0 or currentIndex == 1:
                if sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0] == sorted5cards[currentIndex + 2][
                    0] == \
                        sorted5cards[currentIndex + 3][0]:
                    addToIndex = 4
                    points += 4
                elif sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0] == \
                        sorted5cards[currentIndex + 2][0]:
                    addToIndex = 3
                    points += 3
                elif sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0]:
                    addToIndex = 2
                    points += 2
                else:
                    addToIndex = 1
            if currentIndex == 2:
                if sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0] == sorted5cards[currentIndex + 2][
                    0]:
                    addToIndex = 3
                    points += 3
                elif sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0]:
                    addToIndex = 2
                    points += 2
                else:
                    addToIndex = 1
            if currentIndex == 3:
                if sorted5cards[currentIndex][0] == sorted5cards[currentIndex + 1][0]:
                    addToIndex = 2
                    points += 2
                else:
                    addToIndex = 1
            currentIndex += addToIndex
        return points