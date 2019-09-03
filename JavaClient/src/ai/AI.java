package ai;

import team.koala.chillin.client.RealtimeAI;
import ks.KSObject;
import ks.models.*;
import ks.commands.*;


public class AI extends RealtimeAI<World, KSObject> {

	public AI(World world) {
		super(world);
	}

	@Override
	public void initialize() {
		System.out.println("initialize");
	}

	@Override
	public void decide() {
		System.out.println("decide");

        if (this.mySide.equals("Pacman")) {
        	int randIndex = (int) (Math.random() * EDirection.values().length);
        	EDirection randDir = EDirection.values()[randIndex];
            changePacmanDirection(randDir);
        }

        else if (this.mySide.equals("Ghost")) {
            for (Ghost ghost : this.world.getGhosts()) {
            	int randIndex = (int) (Math.random() * EDirection.values().length);
            	EDirection randDir = EDirection.values()[randIndex];
            	changeGhostDirection(ghost.getId(), randDir);
            }
        }
	}


	public void changePacmanDirection(EDirection direction)
	{
		final ECommandDirection dir = ECommandDirection.of(direction.getValue()); 
		this.sendCommand(new ChangePacmanDirection() {
			{ direction = dir; }
		});
	}

	public void changeGhostDirection(int id, EDirection direction)
	{
		final int ghostId = id;
		final ECommandDirection dir = ECommandDirection.of(direction.getValue()); 
		this.sendCommand(new ChangeGhostDirection() {
			{ id = ghostId; direction = dir; }
		});
	}
}
