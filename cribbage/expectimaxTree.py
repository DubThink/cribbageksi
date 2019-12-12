from cribbage.deck import peg_val
from copy import deepcopy
import cribbage.deck

class node:
    children = []
    utility = 0
    card = None
    myScore = 0
    opponantScore = 0
    sumFromPlay = 0

    def __init__(self, card, utility):
        self.card = card
        self.utility = utility

    def addChild(self, childNode):
        self.children.append(childNode)

    def debug(self):
        print("Debugging Info for Normal Node:")
        print("Children: ", self.children)
        print("Utility: ", self.utility)
        print("Card:", self.card)


class chanceNode:
    children = []
    utility = 0
    card = None
    probability = 0

    def __init__(self, card, probability):
        self.utility = 0

    def debug(self):
        print("Debuggin Info for Chance Node:")
        print("Children: ", self.children)
        print("Utility: ", self.utility)
        print("Card:", self.card)

    def addChild(self, childNode):
        self.children.append(childNode)


class expectimaxTree:
    chanceNode = chanceNode
    node = node

    # Initializes an expectimax tree of a specified depth
    def __init__(self, hand, sequence, current_sum, tree_depth):

        # Initialize tree
        print("hand:", hand)
        print("sequence:", sequence)
        print("current sum:", current_sum)
        root = self.node(None, 0)

        # Consider all cards in hand that are legal moves
        legal_moves = []
        for card in hand:
            if peg_val(card) + current_sum <= 31:
                legal_moves.append(card)

        # Put valid cards in hand into tree
        for i in legal_moves:
            newNode = self.node(i, 0)
            newNode.sumFromPlay = current_sum + i[0]
            root.addChild(newNode)


        # Get deck of cards
        whole_deck = []
        deck = cribbage.deck.Deck()
        for i in deck.cards:
            whole_deck.append(i)
        print("Whole deck: ", whole_deck)

        # Remove known cards from deck
        for i in hand:
            whole_deck.remove(i)
        for i in sequence:
            whole_deck.remove(i)

        # For each level 2 node, put in prob nodes with legal moves
        for i in root.children:
            # Get rid of illegal or used cards
            card_deck = deepcopy(whole_deck)
            if node.card in card_deck:
                card_deck.remove(node.card)
            for card in card_deck:
                if node.sumFromPlay + card[0] > 31 and card in card_deck:
                    card_deck.remove(card)

            # Make new nodes in children of current node using prob nodes
            for card in card_deck:
                newChanceNode = self.chanceNode(card, 1/len(card_deck))
                i.debug()
                i.addChild(newChanceNode)





    # Searches the expectimax tree and recommends the card to be played
    # 0 for  no risk, 1 for medium risk, 2 for high risk
    def recommendCard(self, risk):
        pass




