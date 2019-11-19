from cribbage.Agents import RandomCribbageAgent, HumanAgent, GreedyCribbageAgent
from cribbage.cribbageGame import CribbageGame


if __name__ == "__main__":
    CribbageGame(RandomCribbageAgent(),GreedyCribbageAgent()).play_game()