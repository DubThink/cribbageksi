import heapq
from itertools import combinations

def score_hand(hand4cards, cutcard):
    """
    Returns the total point value of a 4 card hand with the given cut card
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :return: integer point value of the hand
    """

    total_points = 0
    total_points += right_jack(hand4cards,cutcard)
    total_points += flush(hand4cards,cutcard)

    sorted5cards=sort_cards(hand4cards,cutcard)

    total_points += two_card_fifteens(sorted5cards)
    total_points += three_card_fifteens(sorted5cards)
    total_points += four_card_fifteens(sorted5cards)
    total_points += five_card_fifteens(sorted5cards)
    total_points += runs(sorted5cards)
    total_points += pairs(sorted5cards)

    return total_points


def sort_cards(hand4cards,cutcard):
    """
    puts the hand of 4 cards and the cut card into one sorted hand
    :param hand4cards: 4 cards in the player's hand
    :param cutcard: cut card
    :return: sorted five card hand
    """
    hand_queue = []
    hand4cards.append(cutcard)
    for i in range(5):
        heapq.heappush(hand_queue, hand4cards[i])
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
        if card[0] == 11 and cutcard[1] == card[1]:  # if card in hand is a Jack and its suit matches the cut card
            points += 1
    return points


def flush(hand4cards, cutcard):
    """
    Returns the point value from flushes in the given hand
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :return: points from flushes
    """
    points=0
    # flushes
    if hand4cards[0][1] == hand4cards[1][1] == hand4cards[2][1] == hand4cards[3][1]:
        points += 4
        if hand4cards[0][1] == cutcard[1]:
            points += 1
    return points

def two_card_fifteens(sorted5cards):
    """
    Returns the point value of pairs of cards that sum to 15
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from two card 15's
    """
    points=0
    index_combinations2 = combinations([0,1,2,3,4], 2)
    for combination in list(index_combinations2):
        value1 = sorted5cards[combination[0]][0]
        if value1 in range(11, 14):
            value1 = 10
        value2 = sorted5cards[combination[1]][0]
        if value2 in range(11, 14):
            value2 = 10
        if value1 + value2 == 15:
            points += 2
    return points

def three_card_fifteens(sorted5cards):
    """
    Returns the point value of 3 cards that sum to 15
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from three card 15's
    """
    points=0
    index_combinations3 = combinations([0, 1, 2, 3, 4], 3)
    for combination in list(index_combinations3):
        value1 = sorted5cards[combination[0]][0]
        if value1 in range(11, 14):
            value1 = 10
        value2 = sorted5cards[combination[1]][0]
        if value2 in range(11, 14):
            value2 = 10
        value3 = sorted5cards[combination[2]][0]
        if value3 in range(11, 14):
            value3 = 10
        if value1 + value2 + value3 == 15:
            points += 2
    return points

def four_card_fifteens(sorted5cards):
    """
    Returns the point value of 4 cards that sum to 15
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from four card 15's
    """
    points=0
    index_combinations4 = combinations([0, 1, 2, 3, 4], 4)
    for combination in list(index_combinations4):
        value1 = sorted5cards[combination[0]][0]
        if value1 in range(11, 14):
            value1 = 10
        value2 = sorted5cards[combination[1]][0]
        if value2 in range(11, 14):
            value2 = 10
        value3 = sorted5cards[combination[2]][0]
        if value3 in range(11, 14):
            value3 = 10
        value4 = sorted5cards[combination[3]][0]
        if value4 in range(11, 14):
            value4 = 10
        if value1 + value2 + value3 + value4 == 15:
            points += 2
    return points

def five_card_fifteens(sorted5cards):
    """
    Returns the point value of 5 cards that sum to 15
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from five card 15's
    """
    points=0
    sum=0
    for i in range(5):
        sum+=sorted5cards[i][0]
    if sum==15:
        points+=2
    return points


def runs(sorted5cards):
    """
    Returns the point value from runs
    :param sorted5cards: sorted list of 4 cards in the player's hand and the cut card
    :return: points from runs
    """
    points=0
    for start_index in range(3):
        next_index=start_index+1
        consecutive_cards_count = 1
        duplicates_count = 0
        while next_index<5:
            if sorted5cards[start_index][0] == sorted5cards[next_index][0]:
                duplicates_count += 1
            elif sorted5cards[start_index][0] == sorted5cards[next_index][0] - 1:
                consecutive_cards_count += 1
            else:
                break
            start_index = next_index
            next_index += 1
        multiplier = 1
        if duplicates_count > 0:
            multiplier = duplicates_count+1
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
    points=0
    start_card_index = 0
    while start_card_index < 4:
        index = start_card_index + 1
        for i in range(index, 5):
            if sorted5cards[start_card_index][0] == sorted5cards[i][0]:
                points += 2
        start_card_index += 1
    return points


def expected_hand_value(hand4cards,discard2cards):
    card_counts=[]
    for i in range(14):
        card_counts.append(4)
    six_cards=hand4cards.append(discard2cards[0],discard2cards[1])
    for card in six_cards:
        value=card[0]
        card_counts[value-1] -= 1

    expected_value=0

    for i in range (14):
        hand_value=score_hand(hand4cards,(i,1))
        probability=card_counts[i]/46
        expected_value += (hand_value*probability)

    return expected_value
