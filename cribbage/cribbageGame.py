from cribbage.deck import Deck, card_to_string, peg_val
from copy import deepcopy
from cribbage.scoreHand import score_hand

PAIR_SCORES = {2: ("Pair", 2), 3: ("3 of a kind", 6), 4: ("Four of a kind", 12)}


def min_card(hand):
    """
    :returns a card with the minimum pegging value
    """
    c = hand[0]
    for i in range(1, len(hand)):
        if peg_val(hand[i]) < peg_val(c):
            c = hand[i]
    return c


def min_card_val(hand):
    """
    :returns the pegging value of the minimum card
    """
    return min([peg_val(c) for c in hand])


def can_peg(hand, total):
    """
    :returns true if a hand has a card that can be played
    :param hand: the hand to evaluate
    :param total: the total score on the table
    """
    if len(hand) == 0:
        return False
    return min_card_val(hand) + total <= 31


class CribbageGame:
    """
    A game of cribbage
    The game is run by calling play_game()
    The game can only be run once.
    To disable most of the printout, set game.verbose to false
    """
    def __init__(self, agent_a, agent_b):
        self.agent_a = agent_a
        self.agent_b = agent_b
        self.a_score = 0
        self.b_score = 0
        self.verbose = True

    def play_game(self):
        """
        The main gameplay function
        To get the scores post game, check game.a_score and game.b_score
        """
        a_is_dealer = True
        while not self.run_round(a_is_dealer):
            a_is_dealer = not a_is_dealer

    def run_round(self, a_is_dealer):
        """
        Runs a round of cribbage between agent_a and agent_b
        :param a_is_dealer: if a is the dealer and gets the crib
        :return: true if the game was won, false if otherwise
        """

        # setup
        deck = Deck()
        deck.shuffle()
        hand_a = deck.drawCards(6)
        hand_b = deck.drawCards(6)
        crib = []

        # discards
        discard_a = self.agent_a.discard_crib(deepcopy(hand_a), a_is_dealer)
        if len(discard_a) != 2:
            raise IllegalMoveException("Agent discarded more or less than 2 cards.")
        if discard_a[0] not in hand_a or discard_a[1] not in hand_a:
            raise IllegalMoveException("Agent discarded a card it did not own.")
        if discard_a[0] == discard_a[1]:
            raise IllegalMoveException("Agent discarded the same card twice.")

        discard_b = self.agent_b.discard_crib(deepcopy(hand_b), not a_is_dealer)
        if len(discard_b) != 2:
            raise IllegalMoveException("Agent discarded more or less than 2 cards.")
        if discard_b[0] not in hand_b or discard_b[1] not in hand_b:
            raise IllegalMoveException("Agent discarded a card it did not own.")
        if discard_b[0] == discard_b[1]:
            raise IllegalMoveException("Agent discarded the same card twice.")

        crib = [discard_a[0], discard_a[1], discard_b[0], discard_b[1]]
        hand_a.remove(discard_a[0])
        hand_a.remove(discard_a[1])
        hand_b.remove(discard_b[0])
        hand_b.remove(discard_b[1])

        # cut card
        cut_card = deck.drawCard()
        if self.verbose:
            print("The cut card is the", card_to_string(cut_card))
        if cut_card[0] == 11:  # if the a jack is turned
            self.score_points(2, "His heels", a_is_dealer)

        # run pegging
        if self.pegging(deepcopy(hand_a), deepcopy(hand_b), not a_is_dealer):
            # if the game was won during pegging, return true
            return True

        self.print_scores()

        if self.verbose:
            print("The cut card is the", card_to_string(cut_card))
        # score non-dealer's hand
        if a_is_dealer:
            if self.verbose:
                print("B's hand:")
                print(", ".join([card_to_string(c) for c in hand_b]))
            self.score_hand(hand_b, cut_card, False)
        else:
            if self.verbose:
                print("A's hand:")
                print(", ".join([card_to_string(c) for c in hand_a]))
            self.score_hand(hand_a, cut_card, True)

        if self.game_over():
            return True

        # score dealer's hand
        if not a_is_dealer:
            if self.verbose:
                print("B's hand:")
                print(", ".join([card_to_string(c) for c in hand_b]))
            self.score_hand(hand_b, cut_card, False)
        else:
            if self.verbose:
                print("A's hand:")
                print(", ".join([card_to_string(c) for c in hand_a]))
            self.score_hand(hand_a, cut_card, True)

        if self.game_over():
            return True

        # score the crib
        if self.verbose:
            print("The crib, which belongs to %s:" % ("A" if a_is_dealer else "B"))
            print(", ".join([card_to_string(c) for c in crib]))
        self.score_hand(crib, cut_card, a_is_dealer, True)

        if self.game_over():
            return True

        self.print_scores()

        return False

    def game_over(self):
        """
        :returns true if the game was won
        """
        if self.a_score > 120:
            winner = "A"
        elif self.b_score > 120:
            winner = "B"
        else:
            return False
        print("GAME OVER!")
        print(winner + " passed a score of 120 to win.")
        self.print_scores()
        return True

    def print_scores(self):
        if self.verbose:
            print("Scores:\nA: %d\nB: %d\n" % (self.a_score, self.b_score))

    def score_points(self, amount, reason, is_a):
        """
        scores points for a player
        :param amount: the amount of points scored
        :param reason: the reason for the points as a string. Prints in the format of (amount) for (reason)
        :param is_a: if the player who scored points was a
        """
        if is_a:
            self.a_score += amount
        else:
            self.b_score += amount
        if self.verbose:
            print("%s for %d (%s)" % (reason, amount, "A" if is_a else "B"))

    def pegging(self, hand_a, hand_b, is_a):
        """
        :param hand_a: the hand of player a. Must be a copy/mutable
        :param hand_b: the hand of player b. Must be a copy/mutable
        :param is_a: a starts the pegging
        :returns true if the game was won
        """
        #
        # next_player = hand_b if a_goes_first else hand_a
        total = 0
        seq = []

        while True:
            player = self.agent_a if is_a else self.agent_b
            hand = hand_a if is_a else hand_b
            # the current player can play
            pick = player.pegging_move(deepcopy(hand), deepcopy(seq), total)
            if can_peg(hand, total):
                # a card should be played
                if pick is None:
                    raise IllegalMoveException("Must play a card if able to. data:" + str(
                        (deepcopy(hand), deepcopy(seq), total)) + "   player " + ("A" if is_a else "B"))
                if pick not in hand:
                    raise IllegalMoveException("Must play a card from your hand")
                if peg_val(pick) + total > 31:
                    raise IllegalMoveException("Cannot play a card resulting in a sum over 31")
                seq.append(pick)
                hand.remove(pick)
                total += peg_val(pick)
                if self.verbose:
                    print("%s played %s for %d" % ("A" if is_a else "B", card_to_string(pick), total))
                    # print("total:", total)
                    # print("sequence:", ", ".join([card_to_string(c) for c in seq]))
                self.score_pegging(seq, total, is_a)
                if self.game_over():
                    return True
            else:
                if pick is not None:
                    raise IllegalMoveException("Played a card that brought the total over 31.")
            if not can_peg(hand_a, total) and not can_peg(hand_b, total):
                # make sure neither player tries to play a card
                pick_a = self.agent_a.pegging_move(deepcopy(hand_a), deepcopy(seq), total)
                pick_b = self.agent_b.pegging_move(deepcopy(hand_b), deepcopy(seq), total)
                if pick_a is not None or pick_b is not None:
                    raise IllegalMoveException("Played a card that brought the total over 31.")
                # neither person can go
                self.score_points(1, "Last card", is_a)
                if self.game_over():
                    return True
                total = 0
                seq = []

            is_a = not is_a

            if len(hand_a) == 0 and len(hand_b) == 0:
                # pegging is finished
                return False

    def score_pegging(self, seq, total, is_a):
        """
        Scores a single play in pegging
        :param seq:
        :param total:
        :param is_a:
        :return:
        """
        if len(seq) < 2:
            return
        if total == 15:
            self.score_points(2, "Fifteen", is_a)
        if total == 31:
            self.score_points(1, "Thirty one", is_a)
        run_up = 0
        run_down = 0
        continue_run = True
        pair = 1
        continue_pair = True
        top_card = seq[-1]
        for i in range(len(seq) - 2, -1, -1):
            if continue_pair:
                if seq[i][0] == top_card[0]:
                    pair += 1
                else:
                    continue_pair = False

            if continue_run:
                if seq[i][0] == top_card[0] - 1 - run_down:
                    # card we're looking at is part of a sequence down
                    run_down += 1
                elif seq[i][0] == top_card[0] + 1 + run_up:
                    run_up += 1
                else:
                    continue_run = False
        if pair in PAIR_SCORES:
            self.score_points(PAIR_SCORES[pair][1], PAIR_SCORES[pair][0], is_a)
        run_total = run_up + run_down + 1
        if run_total > 2:
            self.score_points(run_total, "A run of %d" % run_total, is_a)

        return 0

    def pegging_round(self, hand_a, hand_b, a_goes_first):
        pass

    def score_hand(self, hand4cards, cutcard, is_a, is_crib=False):
        """
        scores points from a given hand
        :param hand4cards: the hand's cards
        :param cutcard: the cut card
        :return:
        """
        self.score_points(score_hand(hand4cards, cutcard, is_crib), "Their cards", is_a)


class IllegalMoveException(Exception):
    pass
