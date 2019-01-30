#include "ai.h"

#include <ctime>
#include <vector>
#include <iostream>

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
    simple_ai::ai = this;
    srand(time(0));
}

AI::~AI()
{
    if (board)
    {
        for (int i = 0; i < world->height(); i++)
            delete[] board[i];
        delete[] board;
    }
}

void AI::initialize()
{
    cout << "initialize" << endl;
    board = new int*[world->height()];
    for (int i = 0; i < world->height(); i++)
        board[i] = new int[world->width()];

    for (int i = 0; i < world->height(); i++)
        for (int j = 0; j < world->width(); j++)
            board[i][j] = world->ref_board()[i][j];

    simple_ai::initialize(
        world->width(),
        world->height(),
        world->ref_scores()[mySide],
        world->ref_scores()[otherSide],
        board,
        &world->ref_pacman(),
        &world->ref_ghosts()[otherSide][0],
        world->ref_ghosts()[otherSide].size(),
        &world->ref_constants(),
        mySide,
        otherSide,
        currentCycle,
        cycleDuration
    );
}

void AI::decide()
{
    cout << "decide" << endl;
    simple_ai::decide(
        world->width(),
        world->height(),
        world->ref_scores()[mySide],
        world->ref_scores()[otherSide],
        board,
        &world->ref_pacman(),
        &world->ref_ghosts()[otherSide][0],
        world->ref_ghosts()[otherSide].size(),
        &world->ref_constants()[0],
        world->ref_constants().size(),
        mySide,
        otherSide,
        currentCycle,
        cycleDuration
    );
}

int AI::getRandInt(int start, int end)
{
    return (rand() % (end - start + 1)) + start;
}


void AI::sendCommand(ks::KSObject *command)
{
    BaseAI::sendCommand(command);
}
