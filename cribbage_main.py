from cribbage.Agents import RandomCribbageAgent, HumanAgent, GreedyCribbageAgent, AdvancedAgent
from cribbage.cribbageGame import CribbageGame


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


if __name__ == "__main__":
    run_trials(GreedyCribbageAgent(), AdvancedAgent(), 100)
