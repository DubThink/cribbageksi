from cribbage.deck import Deck
from copy import deepcopy

class CribbageGame:
    def __init__(self, agentA, agentB):
        self.agentA = agentA
        self.agentB = agentB

    def run_round(self, a_is_dealer):
        deck = Deck()
        deck.shuffle()
        hand_a = deck.drawCards(6)
        hand_b = deck.drawCards(6)
        crib=[]
        discard_a = self.agentA.discard_crib(deepcopy(hand_a), a_is_dealer)
        if len(discard_a) != 2:
            raise IllegalMoveException("Agent discarded more or less than 2 cards.")
        if discard_a[0] not in hand_a or discard_a[1] not in hand_a:
            raise IllegalMoveException("Agent discarded a card it did not own.")
        if discard_a[0]==discard_a[1]:
            raise IllegalMoveException("Agent discarded the same card twice.")

        discard_b = self.agentB.discard_crib(deepcopy(hand_b), not a_is_dealer)

class IllegalMoveException(Exception):
    pass

