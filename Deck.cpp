//
// Created by benja on 11/6/2019.
//

#include <cstdlib>
#include <sstream>
#include <iostream>
#include "Deck.h"


const char* valString(int val){
    switch(val){
        case 1:
            return "Ace";
        case 2:
            return "2";
        case 3:
            return "3";
        case 4:
            return "4";
        case 5:
            return "5";
        case 6:
            return "6";
        case 7:
            return "7";
        case 8:
            return "8";
        case 9:
            return "9";
        case 10:
            return "10";
        case 11:
            return "Jack";
        case 12:
            return "Queen";
        case 13:
            return "King";
        default:
            return "X";

    }
}

const char* suitString(Suit suit){
    switch(suit){
        case CLUBS:
            return "clubs";
        case SPADES:
            return "spades";
        case HEARTS:
            return "hearts";
        case DIAMONDS:
            return "diamonds";

    }
}

Deck::Deck(){
    cards.reserve(52);
    for(int i=1;i<14;i++){
        cards.emplace_back(Card(Suit::DIAMONDS,i));
        cards.emplace_back(Card(Suit::SPADES,i));
        cards.emplace_back(Card(Suit::HEARTS,i));
        cards.emplace_back(Card(Suit::CLUBS,i));
    }
}

void Deck::shuffle() {
    for(int i=0;i<cards.size();i++){
        // swap with one of the numbers in the array past where we are
        int swapidx = (rand()%(cards.size()-i))+i;
        if(swapidx==i)continue;
        Card tmp=cards[swapidx];
        cards[swapidx]=cards[i];
        cards[i]=tmp;
    }
}

Card Deck::drawCard() {
    Card ret=cards.back();
    cards.pop_back();
    return ret;
}

void Deck::printDeck() {
    std::cout<<std::endl;
    for (auto &card : cards) {
        std::cout<< card.toString()<<",\n";
    }
    std::cout<<std::endl;

}

std::string Card::toString() {
    std::stringstream fmt;
    fmt << valString(value)<<" of "<<suitString(suit);
    return fmt.str();
}
