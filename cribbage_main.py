from cribbage.deck import Deck, Suit
from cribbage.Agents import CribbageAgent, HumanAgent
from cribbage.cribbageGame import CribbageGame


if __name__ == "__main__":
    CribbageGame(CribbageAgent(),CribbageAgent()).play_game()