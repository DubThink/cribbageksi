from cribbage.deck import Deck, card_to_string, peg_val
from copy import deepcopy
from cribbage.scoreHand import score_hand

PAIR_SCORES={2:("Pair",2),3:("3 of a kind",6),4:("Four of a kind",12)}


def min_card(hand):
    """
    Returns a card with the minimum pegging value
    """
    c = hand[0]
    for i in range(1,len(hand)):
        if peg_val(hand[i]) < peg_val(c):
            c = hand[i]
    return c


def min_card_val(hand):
    """
    returns the pegging value of the minimum card
    """
    return min([peg_val(c) for c in hand])


def can_peg(hand, total):
    if len(hand) == 0:
        return False
    return min_card_val(hand) + total <= 31


class CribbageGame:
    def __init__(self, agent_a, agent_b):
        self.agent_a = agent_a
        self.agent_b = agent_b
        self.a_score = 0
        self.b_score = 0
        self.verbose = True

    def play_game(self):
        a_is_dealer = True
        while not self.run_round(a_is_dealer):
            a_is_dealer = not a_is_dealer

    def run_round(self, a_is_dealer):
        """
        Runs a round of cribbage between agent_a and agent_b
        :param a_is_dealer: if a is the dealer and gets the crib
        :return:
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
        crib = [discard_a[0],discard_a[1],discard_b[0],discard_b[1]]
        hand_a.remove(discard_a[0])
        hand_a.remove(discard_a[1])
        hand_b.remove(discard_b[0])
        hand_b.remove(discard_b[1])

        # cut card
        cut_card = deck.drawCard()
        if self.verbose:
            print("The cut card is the",card_to_string(cut_card))
        if cut_card[0] is 11:  # if the a jack is turned
            self.score_points(2, "His heels", a_is_dealer)

        if self.pegging(deepcopy(hand_a), deepcopy(hand_b), a_is_dealer):
            return True

        self.print_scores()
        # print("DEBUG",hand_a,hand_b)
        if a_is_dealer:
            print("B's hand:")
            print(", ".join([card_to_string(c) for c in hand_b]))
            self.score_hand(hand_b, cut_card, False)
        else:
            print("A's hand:")
            print(", ".join([card_to_string(c) for c in hand_a]))
            self.score_hand(hand_b, cut_card, True)

        if self.game_over():
            return True

        print("The crib, which belongs to %s:" % ("A" if a_is_dealer else "B"))
        self.score_hand(crib, cut_card, a_is_dealer, True)

        if self.game_over():
            return True

        if not a_is_dealer:
            print("B's hand:")
            print(", ".join([card_to_string(c) for c in hand_b]))
            self.score_hand(hand_b, cut_card, False)
        else:
            print("A's hand:")
            print(", ".join([card_to_string(c) for c in hand_a]))
            self.score_hand(hand_b, cut_card, True)

        if self.game_over():
            return True

        self.print_scores()

        return False

    def game_over(self):
        if self.a_score>120:
            winner = "A"
        elif self.b_score>120:
            winner = "B"
        else:
            return False
        print("GAME OVER!")
        print(winner + "passed a score of 120 to win.")
        self.print_scores()
        return True

    def print_scores(self):
        if self.verbose:
            print("Scores:\nA: %d\nB: %d\n" % (self.a_score, self.b_score))

    def score_points(self,amount, reason, is_a):
        if is_a:
            self.a_score += amount
        else:
            self.b_score += amount
        if self.verbose:
            print("%s for %d (%s)"%(reason, amount, "A" if is_a else "B"))

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
            if can_peg(hand, total):
                pick = player.pegging_move(deepcopy(hand), deepcopy(seq), total)
                # a card should be played
                if pick is None:
                    raise IllegalMoveException("Must play a card if able to. data:"+str((deepcopy(hand), deepcopy(seq), total))+"   player "+("A" if is_a else "B"))
                if pick not in hand:
                    raise IllegalMoveException("Must play a card from your hand")
                if peg_val(pick) + total > 31:
                    raise IllegalMoveException("Cannot play a card resulting in a sum over 31")
                seq.append(pick)
                hand.remove(pick)
                total += peg_val(pick)
                if self.verbose:
                    print("%s played %s for %d" % ("A" if is_a else "B",card_to_string(pick),total))
                    # print("total:", total)
                    # print("sequence:", ", ".join([card_to_string(c) for c in seq]))
                self.score_pegging(seq, total, is_a)
                if self.game_over():
                    return True
            if not can_peg(hand_a,total) and not can_peg(hand_b,total):
                # neither person can go
                self.score_points(1,"Last card", is_a)
                if self.game_over():
                    return True
                total=0
                seq=[]

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
        if len(seq)<2:
            return
        if total == 15:
            self.score_points(2,"Fifteen", is_a)
        if total == 31:
            self.score_points(1,"Thirty one",is_a)
        run_up=0
        run_down=0
        continue_run=True
        pair=1
        continue_pair = True
        top_card=seq[-1]
        for i in range(len(seq)-2,-1,-1):
            if continue_pair:
                if seq[i] == top_card:
                    pair += 1
                else:
                    continue_pair = False

            if continue_run:
                if seq[i][0]==top_card[0]-1-run_down:
                    # card we're looking at is part of a sequence down
                    run_down += 1
                elif seq[i][0]==top_card[0]+1+run_up:
                    run_up += 1
                else:
                    continue_run = False
        if pair in PAIR_SCORES:
            self.score_points(PAIR_SCORES[pair][1],PAIR_SCORES[pair][0],is_a)
        run_total = run_up+run_down+1
        if run_total>2:
            self.score_points(run_total,"A run of %d"%run_total,is_a)

        return 0

    def pegging_round(self,hand_a,hand_b,a_goes_first):
        pass

    def score_hand(self, hand4cards, cutcard, is_a, is_crib=False):
        self.score_points(score_hand(hand4cards,cutcard),"Their cards",is_a)


class IllegalMoveException(Exception):
    pass

