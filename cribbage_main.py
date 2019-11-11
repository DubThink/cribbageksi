from cribbage.deck import Deck, Suit
from cribbage.cribbageAgent import CribbageAgent
from cribbage.cribbageGame import CribbageGame


if __name__ == "__main__":
    CribbageGame(CribbageAgent(),CribbageAgent()).run_round(True)