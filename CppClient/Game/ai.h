#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::RealtimeAI<ks::models::World*>
{
public:
    AI(ks::models::World *world);
    ~AI();

    void initialize();
    void decide();

    void changePacmanDirection(ks::models::EDirection direction);
    void changeGhostDirection(int id, ks::models::EDirection direction);
};

#endif // AI_H
