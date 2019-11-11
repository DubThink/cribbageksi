import heapq

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


    # 15's
    start_card_index = 0
    while start_card_index < 4:
        index = start_card_index + 1
        for i in range(index, 5):
            value1 = sorted5cards[start_card_index][0]
            if value1 in range(11,14):
                value1 = 10
            value2 = sorted5cards[i][0]
            if value2 in range(11,14):
                value2 = 10
            if value1 + value2 == 15:
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
    start_card_index = 0
    while start_card_index < 4:
        index=start_card_index+1
        for i in range(index, 5):
            if sorted5cards[start_card_index][0] == sorted5cards[i][0]:
                points += 2
        start_card_index += 1

    return points


