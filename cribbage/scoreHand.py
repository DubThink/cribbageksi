import heapq
from itertools import combinations

def score_hand(hand4cards, cutcard):
    """
    Returns the point value of a 4 card hand with the given cut card
    :param hand4cards: the 4 cards in the player's hand
    :param cutcard: cut card
    :return: integer point value of the hand
    """

    points = 0


    # right jack
    for card in hand4cards:
        if card[0] == 11 and cutcard[1] == card[1]:  # if card in hand is a Jack and its suit matches the cut card
            points += 1

    # flushes
    if hand4cards[0][1] == hand4cards[1][1] == hand4cards[2][1] == hand4cards[3][1]:
        points += 4
        if hand4cards[0][1] == cutcard[1]:
            points += 1


    # create list of sorted 5 card hand
    hand_queue = []
    hand4cards.append(cutcard)
    for i in range(5):
        heapq.heappush(hand_queue, hand4cards[i])
    sorted5cards = heapq.nsmallest(5, hand_queue)


    #pairs 15's
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
            
    #3 card 15's
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

    # 4 card 15's
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

    # 5 card 15's
    sum=0
    for i in range(5):
        sum+=sorted5cards[i][0]
    if sum==15:
        points+=2

    # runs
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

    # pairs/3 of a kind/4 of a kind
    start_card_index = 0
    while start_card_index < 4:
        index=start_card_index+1
        for i in range(index, 5):
            if sorted5cards[start_card_index][0] == sorted5cards[i][0]:
                points += 2
        start_card_index += 1

    return points


