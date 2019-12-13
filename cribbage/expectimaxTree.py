from cribbage.deck import peg_val
from copy import deepcopy
import cribbage.deck

class node:
    def __init__(self, card, utility):
        self.children = []
        self.utility = 0
        self.myScore = 0
        self.opponantScore = 0
        self.sumFromPlay = 0
        self.card = card

    def addChild(self, childNode):
        self.children.append(childNode)

    def debug(self):
        print("Debugging Info for Normal Node:")
        print("Children: ", self.children)
        print("Utility: ", self.utility)
        print("Card:", self.card)

    def getChildren(self):
        return self.children

    def getCard(self):
        return self.card

    def getSumFromPlay(self):
        return self.sumFromPlay

    def setSumFromPlay(self, sum):
        self.sumFromPlay = sum


class chanceNode:
    def __init__(self, card, probability):
        self.children = []
        self.utility = 0
        self.card = card
        self.probability = probability
        self.utility = 0

    def debug(self):
        print("Debuggin Info for Chance Node:")
        print("Children: ", self.children)
        print("Utility: ", self.utility)
        print("Card:", self.card)

    def addChild(self, childNode):
        self.children.append(childNode)

    def getChildren(self):
        return self.children

    def getCard(self):
        return self.card


class expectimaxTree:
    def scoreCalc(self, hand, sequence, current_sum):
        # Calculate the score for playing any specific card
        if len(sequence) > 3:
            cards = [peg_val(sequence[len(sequence) - 1]), peg_val(sequence[len(sequence) - 2]), peg_val(sequence[len(sequence) - 3])]
            cards.sort()
            if cards[0] + 1 in cards and cards[1] + 1 in cards:
                for i in hand:
                    if peg_val(i) == (cards[len(cards) - 1]) + 1 and peg_val(i) + current_sum <= 31:
                        return 4

        # Check 3rd card sequence
        if len(sequence) > 2:
            cards = [peg_val(sequence[len(sequence) - 1]), peg_val(sequence[len(sequence) - 2])]
            cards.sort()
            if cards[0] + 1 in cards:
                for i in hand:
                    if peg_val(i) == cards[len(cards) - 1] + 1 and peg_val(i) + current_sum <= 31:
                        return 3

        # Get sum to 15
        for i in hand:
            # print(i)
            if peg_val(i) + current_sum == 15:
                return 2

        # Play same rank
        if len(sequence) > 0:
            check = sequence[len(sequence) - 1]
            for i in hand:
                if i == check and peg_val(i) + current_sum <= 31:
                    return 2
        return 0


    # Initializes an expectimax tree of a specified depth
    def __init__(self, hand, sequence, current_sum, tree_depth):
        # Initialize tree
        print("hand:", hand)
        print("sequence:", sequence)
        print("current sum:", current_sum)
        root = node(None, 0)

        # Consider all cards in hand that are legal moves
        legal_moves = []
        for card in hand:
            if peg_val(card) + current_sum <= 31:
                legal_moves.append(card)
                newNode = node(card, 0)
                newNode.sumFromPlay = current_sum + card[0]
                root.addChild(newNode)

        print("legal moves: ", legal_moves)
        print("Root's children: ", root.children)


        # Get deck of cards
        whole_deck = []
        deck = cribbage.deck.Deck()
        for i in deck.cards:
            whole_deck.append(i)
        #print("Whole deck: ", whole_deck)

        # Remove known cards from deck
        for i in hand:
            whole_deck.remove(i)
        for i in sequence:
            whole_deck.remove(i)

        # print(root.children)
        # if len(root.children) > 10:
        #     print("Something fucked up")

        # For each level 2 node, put in prob nodes with legal moves
        for cnode in root.children:
            # Get rid of illegal or used cards
            card_deck = deepcopy(whole_deck)
            if cnode.getCard() in card_deck:
                card_deck.remove(cnode.getCard())
            for card in card_deck:
                if cnode.getSumFromPlay() + card[0] > 31 and card in card_deck:
                    card_deck.remove(card)

            # Make new nodes in children of current node using prob nodes
            for card in card_deck:
                newChanceNode = chanceNode(card, 1/len(card_deck))
                cnode.addChild(newChanceNode)

        # Go through all prob nodes and add regular nodes for opponent
        for n in root.getChildren():
            for m in n.getChildren():
                card_deck = deepcopy(whole_deck)
                card_deck.remove(m.getCard())
                for o in card_deck:
                    newNode = node(o, 0)
                    m.addChild(newNode)



    # Searches the expectimax tree and recommends the card to be played
    # 0 for  no risk, 1 for medium risk, 2 for high risk
    def recommendCard(self, risk):
        pass




