# Cribbage Ksi
CribbageKsi is a python-based cribbage ai and environment.

# PEAS

Performace: The agent should be able to win over the random agent 70 to 80% of the time. 

Environment: A simulation Cribbage game environment.

Action: The agent handles the discarding of cards and the pegging process.

Sensory: The agent can knows its hand when it is its turn.


### Week of 11/5

Benjamin: environment, deck

Thy: random discard_card

Liam: pegging

Molly: getting the point value of a hand

### Week of 11/11

Benjamin:

Thy: improving discard_crib to be better than random, write unit tests for random discard_crib and upgraded discard_card, work on heuristic

Liam: improve pegging function

Molly: write tests for score_hand, work on function that generates possible 4-card hands given any 2-card elimination

### Week of 11/18

Benjamin: Fix HumanAgent, write game environment for improved agent versus baseline agent

Molly: Fix scorehand and write tests for scorehand

Thy: implement A* heuristic for bfs for discard crib

Liam: minimax for pegging moves

# AI Techniques

Brief description: For discarding, the agent looks at all possible combinations of 2-card permutations to remove, calculates the possible scores for each permutation and enqueues each permutation into a priority queue according to their score. Pegging uses minimax to look at a maximum of depth 4 to calculate the best possible card to put down. 

List of useful resources: previous labs

AI Technique: Expected Utility Theory

Used to compare values of different lotteries. In our situation, each "lottery" would correspond to one potential four card hand (when deciding which of your six cards to keep), and would consist of the point values and probabilities of each possible cut card. This would allow us to take risk into account. If a player is risk neutral, they would value a lottery at its expected value. However, players can have varying degrees of risk aversion. Using expected utility theory would require us to think about the utilities of getting certain points, rather than just the point values themselves. This utility would be determined by the player's attitudes towards risk, and also their current scores. For example, a player who has a comfortable lead might be willing to take bigger risks when deciding which cards to keep in their hand. Additionally, a player who is farther behind would value getting an additional point more than a player who is farther ahead (diminishing marginal utility).

Resources:
https://en.wikipedia.org/wiki/Expected_utility_hypothesis
http://faculty.econ.ucdavis.edu/faculty/bonanno/PDF/GT_book.pdf    (chapter 5 pg. 169)
https://engineering.purdue.edu/~ipollak/ece302/FALL09/notes/Bernoulli_1738.pdf

This technique is generally used to evaluate financial situations where there is some degree of uncertainty/risk. It can be used for any situation with a set of outcomes and associated probabilities, including our scenario where our agent is trying to decide which four cards to keep. A potential challenge of applying this technique is that the formulas used to adjust the expected value to account for risk aversion might be a little complicated.


