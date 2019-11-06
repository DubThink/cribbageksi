//
// Created by benja on 11/5/2019.
//

#ifndef CRIBBAGEKSI_CRIBBAGEAGENT_H
#define CRIBBAGEKSI_CRIBBAGEAGENT_H

#include <vector>
#include "Deck.h"

class CribbageAgent {
    virtual std::vector<Card> discardCrib(const std::vector<Card> hand,bool isDealer)=0;
    virtual Card peggingStep(int currentSum, const std::vector<Card> sequence,const std::vector<Card> hand)=0;
};
#endif //CRIBBAGEKSI_CRIBBAGEAGENT_H
