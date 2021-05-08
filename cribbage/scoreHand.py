import heapq
import math
import itertools as it
from cribbage.deck import peg_val
from copy import deepcopy


def score_hand(hand4cards, cutcard, is_crib=False):
    """
    Returns the total point value of a 4 card hand with the given cut card
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :param is_crib: if the hand being scored is the crib
    :return: integer point value of the hand
    """
    total_points = 0
    total_points += right_jack(hand4cards, cutcard)
    total_points += flush(hand4cards, cutcard, is_crib)

    sorted5cards = sort_cards(hand4cards, cutcard)

    total_points += fifteens(sorted5cards)
    total_points += runs(sorted5cards)
    total_points += pairs(sorted5cards)

    return total_points


def sort_cards(hand4cards, cutcard):
    """
    puts the hand of 4 cards and the cut card into one sorted hand
    :param hand4cards: 4 cards in the player's hand
    :param cutcard: cut card
    :return: sorted five card hand
    """
    hand_queue = []

    for c in hand4cards:
        heapq.heappush(hand_queue, c)
    heapq.heappush(hand_queue, cutcard)
    sorted5cards = heapq.nsmallest(5, hand_queue)
    return sorted5cards


def right_jack(hand4cards, cutcard):
    """
    Returns the point value from right jacks in the given hand
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :return: 1 point if the hand contains the right jack, 0 otherwise
    """
    points = 0
    # right jack
    for card in hand4cards:
        if card[0] == 11 and cutcard[1] == card[
                1]:  # if card in hand is a Jack and its suit matches the cut card
            points += 1
    return points


def flush(hand4cards, cutcard, is_crib):
    """
    Returns the point value from flushes in the given hand
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :return: points from flushes
    """
    points = 0
    # flushes
    if hand4cards[0][1] == hand4cards[1][1] == hand4cards[2][1] == hand4cards[
            3][1]:
        points += 4
        if hand4cards[0][1] == cutcard[1]:
            points += 1
    if is_crib:
        if points == 4:
            points = 0

    return points


def fifteens(sorted5cards):
    """
    Returns the point value of sets of cards that sum to 15
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from card combinations that sum up to 15's
    """
    combs = it.chain.from_iterable(
        it.combinations(sorted5cards, r) for r in range(1, 6))
    sums = map(lambda x: sum(map(peg_val, x)), combs)
    n15s = filter(lambda x: x == 15, sums)

    return len(tuple(n15s)) * 2


def runs(sorted5cards):
    """
    Returns the point value from runs
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from runs
    """
    points = 0
    for start_index in range(3):
        next_index = start_index + 1
        consecutive_cards_count = 1
        duplicates_count = 0
        while next_index < 5:
            if sorted5cards[start_index][0] == sorted5cards[next_index][0]:
                duplicates_count += 1
            elif sorted5cards[start_index][
                    0] == sorted5cards[next_index][0] - 1:
                consecutive_cards_count += 1
            else:
                break
            start_index = next_index
            next_index += 1
        multiplier = 1
        if duplicates_count > 0:
            multiplier = duplicates_count * 2
        if consecutive_cards_count >= 3:
            points += multiplier * consecutive_cards_count
            break
    return points


def pairs(sorted5cards):
    """
    Returns the point value from pairs (includes 3 of a kind and 4 of a kind)
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from pairs
    """
    points = 0
    start_card_index = 0
    while start_card_index < 4:
        index = start_card_index + 1
        for i in range(index, 5):
            if sorted5cards[start_card_index][0] == sorted5cards[i][0]:
                points += 2
        start_card_index += 1
    return points


def card_counts_list(hand4cards, discard2cards):
    """
    :param hand4cards: a list of 4 cards the player is keeping
    :param discard2cards: a list of the 2 cards the player is planning to discard
    :return:list of how many of each value are still in the 46 cards in the deck
    """
    card_counts = []
    for i in range(13):
        card_counts.append(4)
    for card in hand4cards:
        value = card[0]
        card_counts[value - 1] -= 1
    for card in discard2cards:
        value = card[0]
        card_counts[value - 1] -= 1
    return card_counts


def expected_hand_value(hand4cards, discard2cards, risk):
    """
      Returns the expected point value of a hand (taking into account all possible cut cards)
      :param hand4cards: a list of 4 cards the player is keeping
      :param discard2cards: a list of the 2 cards the player is planning to discard
      :param risk: -1 for risk averse, 0 for risk neutral, 1 for risk loving
      :return: expected point value for the 4 card hand
      """

    card_counts = card_counts_list(hand4cards, discard2cards)
    expected_value = 0

    for i in range(1, 14):
        hand_value = score_hand(hand4cards, (i, 1), False)
        #gets the score of the hand for each possible cut card (not accounting for suits)
        if risk == -1:
            hand_value = math.sqrt(hand_value)
        if risk == 1:
            hand_value = hand_value * hand_value
        probability = card_counts[
            i - 1] / 46  #calculates the probability of drawing that cut card
        expected_value += (
            hand_value * probability
        )  #multiplies the calculated score by the probability of drawing that cut card, adds to total expected value

    return expected_value


def crib_cards_value(discard2cards, yourCrib):
    value = 0
    card1_value = discard2cards[0][0]
    card2_value = discard2cards[1][0]
    if card1_value == card2_value:
        value += 2
    if card1_value + card2_value == 15:
        value += 2
    if card1_value == 5:
        value += 1
    if card2_value == 5:
        value += 1
    if card1_value - card2_value == 1 or card2_value - card1_value == 1:
        value += 1
    if yourCrib:
        return value
    else:
        return -1 * value
