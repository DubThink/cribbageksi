//
// Created by benja on 11/5/2019.
//

#ifndef CRIBBAGEKSI_DECK_H
#define CRIBBAGEKSI_DECK_H
enum Suit{
    CLUBS,
    SPADES,
    HEARTS,
    DIAMONDS
};

struct Card {
    Suit suit;
    int value;
    /**
     * @return 10 for face cards, value for number cards
     */
    int pointValue(){
        return value>10?10:value;
    }
};

class Deck{
private:
    // stuff
public:
    Card drawCard();

};
#endif //CRIBBAGEKSI_DECK_H
