//
// Created by benja on 11/6/2019.
//

#include "CribbageGame.h"

CribbageGame::CribbageGame(CribbageAgent &agentA, CribbageAgent &agentB):
agentA(agentA),agentB(agentB){

}

void CribbageGame::runGame() {
    deck=Deck();
    deck.shuffle();
    std::vector<Card> handA;
    handA.reserve(6);
    std::vector<Card> handB;
    handB.reserve(6);
    for (int i = 0; i < 6; ++i) {
        handA.emplace_back(deck.drawCard());
        handB.emplace_back(deck.drawCard());
    }

}