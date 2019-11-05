//
// Created by benja on 11/5/2019.
//

#ifndef CRIBBAGEKSI_CRIBBAGEAGENT_H
#define CRIBBAGEKSI_CRIBBAGEAGENT_H

#include "Deck.h"

class CribbageAgent {
    virtual Card* discardCrib(const Card* hand,bool isDealer)=0;
    virtual Card peggingStep(int currentSum, const Card* sequence,const Card* hand)=0;
};
#endif //CRIBBAGEKSI_CRIBBAGEAGENT_H
