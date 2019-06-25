#include "ai.h"

#include <iostream>
#include <vector>

#include "effolkronium/random.hpp"

using namespace std;
using Random = effolkronium::random_static;

using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
}

AI::~AI()
{
}

void AI::initialize()
{
    cout << "initialize" << endl;
}

void AI::decide()
{
    cout << "decide" << endl;

    if (this->mySide == "Pacman")
    {
        auto random_direction = Random::get({EDirection::Up, EDirection::Right, EDirection::Down, EDirection::Left});
        changePacmanDirection(random_direction);
    }
    else if (this->mySide == "Ghost")
    {
        for (Ghost &ghost : this->world->ghosts())
        {
            auto random_direction = Random::get({EDirection::Up, EDirection::Right, EDirection::Down, EDirection::Left});
            changeGhostDirection(ghost.id(), random_direction);
        }
    }
}


void AI::changePacmanDirection(EDirection direction)
{
    ChangePacmanDirection cmd;
    cmd.direction((ECommandDirection) direction);
    this->sendCommand(&cmd);
}

void AI::changeGhostDirection(int id, EDirection direction)
{
    ChangeGhostDirection cmd;
    cmd.id(id);
    cmd.direction((ECommandDirection) direction);
    this->sendCommand(&cmd);
}
