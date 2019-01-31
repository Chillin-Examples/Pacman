#include "ai.h"

#include <vector>
#include <iostream>

#include "simple_ai.h"

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
    simple_ai::ai = this;
}

AI::~AI()
{
}

void AI::initialize()
{
    cout << "initialize" << endl;

    simple_ai::initialize(
        world->width(),
        world->height(),
        world->ref_scores()[mySide],
        world->ref_scores()[otherSide],
        world->ref_board(),
        world->ref_pacman(),
        &world->ref_ghosts()[0],
        world->ref_ghosts().size(),
        world->ref_constants(),
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
        world->ref_board(),
        world->ref_pacman(),
        &world->ref_ghosts()[0],
        world->ref_ghosts().size(),
        world->ref_constants(),
        mySide,
        otherSide,
        currentCycle,
        cycleDuration
    );
}

void AI::sendCommand(ks::KSObject *command)
{
    BaseAI::sendCommand(command);
}
