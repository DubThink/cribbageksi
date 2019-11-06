//
// Created by benja on 11/5/2019.
//

#ifndef CRIBBAGEKSI_CRIBBAGEGAME_H
#define CRIBBAGEKSI_CRIBBAGEGAME_H

#include "CribbageAgent.h"

class CribbageGame{
private:
    Deck deck;
    const CribbageAgent &agentA, &agentB;

public:
    CribbageGame(CribbageAgent &agentA,CribbageAgent &agentB);
    void runGame();
};
#endif //CRIBBAGEKSI_CRIBBAGEGAME_H
