from cribbage.deck import Deck, Suit
from cribbage.cribbageAgent import CribbageAgent, HumanAgent
from cribbage.cribbageGame import CribbageGame


if __name__ == "__main__":
    CribbageGame(CribbageAgent(),HumanAgent()).run_round(True)