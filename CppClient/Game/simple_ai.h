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


const int CELL_EMPTY = ECell::Empty;
const int CELL_FOOD = ECell::Food;
const int CELL_SUPER_FOOD = ECell::SuperFood;
const int CELL_WALL = ECell::Wall;

const int DIR_UP = EDirection::Up;
const int DIR_RIGHT = EDirection::Right;
const int DIR_DOWN = EDirection::Down;
const int DIR_LEFT = EDirection::Left;


void change_pacman_direction(int dir)
{
    ChangePacmanDirection changeDir;
    changeDir.direction((ECommandDirection) dir);
    ai->sendCommand(&changeDir);
}

void change_ghost_direction(int id, int dir)
{
    ChangeGhostDirection changeDir;
    changeDir.id(id);
    changeDir.direction((ECommandDirection) dir);
    ai->sendCommand(&changeDir);
}


void initialize(
    int width, int height, int myScore, int otherScore, std::vector<std::vector<ECell>>& board,
    Pacman& Pacman, Ghost ghosts[], int ghostsCount,
    Constants& constants,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
}


void decide(
    int width, int height, int myScore, int otherScore, std::vector<std::vector<ECell>>& board,
    Pacman& Pacman, Ghost ghosts[], int ghostsCount,
    Constants& constants,
    string mySide, string otherSide, int currentCycle, float cycleDuration)
{
    // Write your own AI code here
}

}

#endif // SIMPLE_AI_H
