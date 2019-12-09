class node:
    children = []
    utility = 0
    card = None

    def __init__(self, utility):
        self.utility = utility

    def addChild(self, childNode):
        self.children.append(childNode)


class chanceNode:
    children = []
    utility = 0
    def __init__(self):
        self.utility = 0


class expectimaxTree:
    root = node(0)

    # Initializes an expectimax tree of a specified depth
    def __init__(self, hand, sequence, current_sum, tree_depth):
        pass

    # Searches the expectimax tree and recommends the card to be played
    def recommendCard(self):
        pass




