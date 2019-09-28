using System;

using KoalaTeam.Chillin.Client;
using KS;
using KS.Commands;
using KS.Models;

using KSObject = KS.KSObject;

namespace Game
{
	public class AI : RealtimeAI<World, KSObject>
	{
		private readonly Random random = new Random();

		public AI(World world) : base(world)
		{
		}

		public override void Initialize()
		{
			Console.WriteLine("initialize");
		}

		public override void Decide()
		{
			Console.WriteLine("decide");

			if (this.MySide == "Pacman")
			{
				ChangePacmanDirection((EDirection)random.Next(Enum.GetNames(typeof(EDirection)).Length));
			}
			else if (this.MySide == "Ghost")
			{
				foreach (var ghost in this.World.Ghosts)
					ChangeGhostDirection(
						ghost.Id,
						(EDirection)random.Next(Enum.GetNames(typeof(EDirection)).Length)
					);
			}
		}


		public void ChangePacmanDirection(EDirection direction)
		{
			this.SendCommand(new ChangePacmanDirection() { Direction = (ECommandDirection?)direction });
		}

		public void ChangeGhostDirection(int? id, EDirection direction)
		{
			this.SendCommand(new ChangeGhostDirection() { Id = id, Direction = (ECommandDirection?)direction });
		}
	}
}
