#ifndef SIMPLE_AI_H
#define SIMPLE_AI_H

#include <iostream>
#include <vector>

#include "ks/models.h"
#include "ks/commands.h"

using namespace std;
using namespace ks::models;
using namespace ks::commands;

class AI;


namespace simple_ai {

AI *ai;


void move(int bananaId, int dir)
{
    ai->sendCommand(&move);
}

void initialize(
    int width, int height, int myScore, int otherScore, int **board,
    Banana myBananas[], int myBananasCount, Banana otherBananas[], int otherBananasCount,
    PowerUp powerups[], int powerupsCount, int enter_score,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
}


void decide(
    int width, int height, int myScore, int otherScore, int **board,
    Banana myBananas[], int myBananasCount, Banana otherBananas[], int otherBananasCount,
    PowerUp powerups[], int powerupsCount, int enter_score,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
    
}

}

#endif // SIMPLE_AI_H