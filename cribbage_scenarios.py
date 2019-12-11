from copy import deepcopy

from cribbage.Agents import RandomCribbageAgent, HumanAgent, GreedyCribbageAgent,AdvancedAgent
from cribbage.cribbageGame import CribbageGame
from cribbage.deck import *


def run_trials(agent_a, agent_b, num_trials, verbose=False):
    a_wins = 0
    b_wins = 0
    swap = False
    for i in range(num_trials):

        game = CribbageGame(agent_b if swap else agent_a, agent_a if swap else agent_b)
        game.verbose=verbose
        game.play_game()
        # score_a += game.b_score if swap else game.a_score
        # score_b += game.a_score if swap else game.b_score
        if (game.a_score > game.b_score) is not swap:
            a_wins += 1
        else:
            b_wins += 1
    print("A wins: %d B wins %d" % (a_wins, b_wins))


def run_discard_scenarios(hand, *agents):
    print("\nThe hand is:")
    print(", ".join([card_to_string(c) for c in hand]))
    for agent in agents:
        a_hand = deepcopy(hand)
        a_crib = agent.discard_crib(hand, True)
        a_hand.remove(a_crib[0])
        a_hand.remove(a_crib[1])
        print("If "+str(agent)+" is the dealer, they keep %s, discarding    %s" % (", ".join([card_to_string(c) for c in a_hand]), ", ".join([card_to_string(c) for c in a_crib])))
        b_hand = deepcopy(hand)
        b_crib = agent.discard_crib(hand, False)
        b_hand.remove(b_crib[0])
        b_hand.remove(b_crib[1])
        print("If "+str(agent)+" isn't the dealer, they keep %s, discarding %s" % (", ".join([card_to_string(c) for c in b_hand]), ", ".join([card_to_string(c) for c in b_crib])))


if __name__ == "__main__":

    run_discard_scenarios([(10,HEARTS),(7,HEARTS),(13,SPADES),(10,CLUBS),(10,SPADES),(10,DIAMONDS)],GreedyCribbageAgent())

    #risky agent behaves differently than greedy agent
    run_discard_scenarios([(5,HEARTS),(5,DIAMONDS),(5,SPADES),(10,CLUBS),(9,SPADES),(10,DIAMONDS)],GreedyCribbageAgent())
    run_discard_scenarios([(5,HEARTS),(5,DIAMONDS),(5,SPADES),(10,CLUBS),(9,SPADES),(10,DIAMONDS)],AdvancedAgent())

    run_discard_scenarios([(6,HEARTS),(7,DIAMONDS),(7,SPADES),(2,CLUBS),(2,SPADES),(4,DIAMONDS)],GreedyCribbageAgent())
    run_discard_scenarios([(6,HEARTS),(7,DIAMONDS),(7,SPADES),(2,CLUBS),(2,SPADES),(4,DIAMONDS)],GreedyCribbageAgent())



