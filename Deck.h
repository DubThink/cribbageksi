//
// Created by benja on 11/5/2019.
//

#ifndef CRIBBAGEKSI_DECK_H
#define CRIBBAGEKSI_DECK_H

#include <vector>
#include <string>

enum Suit{
    CLUBS,
    SPADES,
    HEARTS,
    DIAMONDS
};

struct Card {
    Card(Suit suit, int value) : suit(suit), value(value) {}
    Suit suit;
    int value;
    /**
     * @return 10 for face cards, value for number cards
     */
    int pointValue(){
        return value>10?10:value;
    }

    std::string toString();
};

class Deck{
private:
    // stuff
    std::vector<Card> cards;
public:
    Deck();
    Card drawCard();
    void shuffle();
    void printDeck();
};
#endif //CRIBBAGEKSI_DECK_H
