from cribbage.Agents import RandomCribbageAgent, HumanAgent, GreedyCribbageAgent
from cribbage.cribbageGame import CribbageGame


if __name__ == "__main__":
    CribbageGame(GreedyCribbageAgent(),GreedyCribbageAgent()).play_game()