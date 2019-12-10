from cribbage.scoreHand import score_hand, expected_hand_value
import unittest

print("risky hand")
hand = [(11, 1), (5, 2), (5, 3), (5, 4)]
discard=[(3,1),(4,2)]
print("risk loving:")
print(expected_hand_value(hand,discard,1))

print("risk neutral:")
print(expected_hand_value(hand,discard,0))

print("risk averse:")
print(expected_hand_value(hand,discard,-1))


print("safer hand")
hand = [(4, 1), (5, 2), (2, 3), (1, 0)]
discard=[(3,1),(4,2)]
print("risk loving:")
print(expected_hand_value(hand,discard,1))

print("risk neutral:")
print(expected_hand_value(hand,discard,0))

print("risk averse:")
print(expected_hand_value(hand,discard,-1))



risky_hand=[(7, 1), (5, 2), (9, 3), (7, 3)]
safer_hand=[(1, 1), (9, 2), (6, 3), (1, 3)]

discard=[(3,1),(4,2)]

print("comparison:")
print(expected_hand_value(risky_hand,discard,-1))
print(expected_hand_value(_hand,discard,-1))


#class TestScoreHand(unittest.TestCase):


   # def test_risky_agent(self):
    #    hand = [(11, 1), (5, 2), (5, 3), (5, 0)]
     #   discard=[(3,1),(4,2)]
      #  expected_hand_value(hand,discard,1)

