using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Models
{
	public enum ECell
	{
		Empty = 0,
		Food = 1,
		SuperFood = 2,
		Wall = 3,
	}
	
	public enum EDirection
	{
		Up = 0,
		Right = 1,
		Down = 2,
		Left = 3,
	}
	
	public partial class Constants : KSObject
	{
		public int? FoodScore { get; set; }
		public int? SuperFoodScore { get; set; }
		public int? GhostDeathScore { get; set; }
		public int? PacmanDeathScore { get; set; }
		public int? PacmanGiantFormDuration { get; set; }
		public int? MaxCycles { get; set; }
		

		public Constants()
		{
		}
		
		public new const string NameStatic = "Constants";
		
		public override string Name() => "Constants";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize FoodScore
			s.Add((byte)((FoodScore == null) ? 0 : 1));
			if (FoodScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)FoodScore));
			}
			
			// serialize SuperFoodScore
			s.Add((byte)((SuperFoodScore == null) ? 0 : 1));
			if (SuperFoodScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)SuperFoodScore));
			}
			
			// serialize GhostDeathScore
			s.Add((byte)((GhostDeathScore == null) ? 0 : 1));
			if (GhostDeathScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)GhostDeathScore));
			}
			
			// serialize PacmanDeathScore
			s.Add((byte)((PacmanDeathScore == null) ? 0 : 1));
			if (PacmanDeathScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PacmanDeathScore));
			}
			
			// serialize PacmanGiantFormDuration
			s.Add((byte)((PacmanGiantFormDuration == null) ? 0 : 1));
			if (PacmanGiantFormDuration != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PacmanGiantFormDuration));
			}
			
			// serialize MaxCycles
			s.Add((byte)((MaxCycles == null) ? 0 : 1));
			if (MaxCycles != null)
			{
				s.AddRange(BitConverter.GetBytes((int)MaxCycles));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize FoodScore
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				FoodScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				FoodScore = null;
			
			// deserialize SuperFoodScore
			byte tmp1;
			tmp1 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp1 == 1)
			{
				SuperFoodScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				SuperFoodScore = null;
			
			// deserialize GhostDeathScore
			byte tmp2;
			tmp2 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp2 == 1)
			{
				GhostDeathScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				GhostDeathScore = null;
			
			// deserialize PacmanDeathScore
			byte tmp3;
			tmp3 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp3 == 1)
			{
				PacmanDeathScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PacmanDeathScore = null;
			
			// deserialize PacmanGiantFormDuration
			byte tmp4;
			tmp4 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp4 == 1)
			{
				PacmanGiantFormDuration = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PacmanGiantFormDuration = null;
			
			// deserialize MaxCycles
			byte tmp5;
			tmp5 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp5 == 1)
			{
				MaxCycles = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				MaxCycles = null;
			
			return offset;
		}
	}
	
	public partial class Position : KSObject
	{
		public int? X { get; set; }
		public int? Y { get; set; }
		

		public Position()
		{
		}
		
		public new const string NameStatic = "Position";
		
		public override string Name() => "Position";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize X
			s.Add((byte)((X == null) ? 0 : 1));
			if (X != null)
			{
				s.AddRange(BitConverter.GetBytes((int)X));
			}
			
			// serialize Y
			s.Add((byte)((Y == null) ? 0 : 1));
			if (Y != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Y));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize X
			byte tmp6;
			tmp6 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp6 == 1)
			{
				X = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				X = null;
			
			// deserialize Y
			byte tmp7;
			tmp7 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp7 == 1)
			{
				Y = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Y = null;
			
			return offset;
		}
	}
	
	public partial class Agent : KSObject
	{
		public Position Position { get; set; }
		public EDirection? Direction { get; set; }
		

		public Agent()
		{
		}
		
		public new const string NameStatic = "Agent";
		
		public override string Name() => "Agent";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Position
			s.Add((byte)((Position == null) ? 0 : 1));
			if (Position != null)
			{
				s.AddRange(Position.Serialize());
			}
			
			// serialize Direction
			s.Add((byte)((Direction == null) ? 0 : 1));
			if (Direction != null)
			{
				s.Add((byte)((sbyte)Direction));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Position
			byte tmp8;
			tmp8 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp8 == 1)
			{
				Position = new Position();
				offset = Position.Deserialize(s, offset);
			}
			else
				Position = null;
			
			// deserialize Direction
			byte tmp9;
			tmp9 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp9 == 1)
			{
				sbyte tmp10;
				tmp10 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (EDirection)tmp10;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
	
	public partial class Pacman : Agent
	{
		public int? Health { get; set; }
		public int? GiantFormRemainingTime { get; set; }
		

		public Pacman()
		{
		}
		
		public new const string NameStatic = "Pacman";
		
		public override string Name() => "Pacman";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize parents
			s.AddRange(base.Serialize());
			
			// serialize Health
			s.Add((byte)((Health == null) ? 0 : 1));
			if (Health != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Health));
			}
			
			// serialize GiantFormRemainingTime
			s.Add((byte)((GiantFormRemainingTime == null) ? 0 : 1));
			if (GiantFormRemainingTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)GiantFormRemainingTime));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			// deserialize Health
			byte tmp11;
			tmp11 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp11 == 1)
			{
				Health = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Health = null;
			
			// deserialize GiantFormRemainingTime
			byte tmp12;
			tmp12 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp12 == 1)
			{
				GiantFormRemainingTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				GiantFormRemainingTime = null;
			
			return offset;
		}
	}
	
	public partial class Ghost : Agent
	{
		public int? Id { get; set; }
		

		public Ghost()
		{
		}
		
		public new const string NameStatic = "Ghost";
		
		public override string Name() => "Ghost";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize parents
			s.AddRange(base.Serialize());
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			// deserialize Id
			byte tmp13;
			tmp13 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp13 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			return offset;
		}
	}
	
	public partial class World : KSObject
	{
		public int? Width { get; set; }
		public int? Height { get; set; }
		public List<List<ECell?>> Board { get; set; }
		public Dictionary<string, int?> Scores { get; set; }
		public Pacman Pacman { get; set; }
		public List<Ghost> Ghosts { get; set; }
		public Constants Constants { get; set; }
		

		public World()
		{
		}
		
		public new const string NameStatic = "World";
		
		public override string Name() => "World";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Width
			s.Add((byte)((Width == null) ? 0 : 1));
			if (Width != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Width));
			}
			
			// serialize Height
			s.Add((byte)((Height == null) ? 0 : 1));
			if (Height != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Height));
			}
			
			// serialize Board
			s.Add((byte)((Board == null) ? 0 : 1));
			if (Board != null)
			{
				List<byte> tmp14 = new List<byte>();
				tmp14.AddRange(BitConverter.GetBytes((uint)Board.Count()));
				while (tmp14.Count > 0 && tmp14.Last() == 0)
					tmp14.RemoveAt(tmp14.Count - 1);
				s.Add((byte)tmp14.Count);
				s.AddRange(tmp14);
				
				foreach (var tmp15 in Board)
				{
					s.Add((byte)((tmp15 == null) ? 0 : 1));
					if (tmp15 != null)
					{
						List<byte> tmp16 = new List<byte>();
						tmp16.AddRange(BitConverter.GetBytes((uint)tmp15.Count()));
						while (tmp16.Count > 0 && tmp16.Last() == 0)
							tmp16.RemoveAt(tmp16.Count - 1);
						s.Add((byte)tmp16.Count);
						s.AddRange(tmp16);
						
						foreach (var tmp17 in tmp15)
						{
							s.Add((byte)((tmp17 == null) ? 0 : 1));
							if (tmp17 != null)
							{
								s.Add((byte)((sbyte)tmp17));
							}
						}
					}
				}
			}
			
			// serialize Scores
			s.Add((byte)((Scores == null) ? 0 : 1));
			if (Scores != null)
			{
				List<byte> tmp18 = new List<byte>();
				tmp18.AddRange(BitConverter.GetBytes((uint)Scores.Count()));
				while (tmp18.Count > 0 && tmp18.Last() == 0)
					tmp18.RemoveAt(tmp18.Count - 1);
				s.Add((byte)tmp18.Count);
				s.AddRange(tmp18);
				
				foreach (var tmp19 in Scores)
				{
					s.Add((byte)((tmp19.Key == null) ? 0 : 1));
					if (tmp19.Key != null)
					{
						List<byte> tmp20 = new List<byte>();
						tmp20.AddRange(BitConverter.GetBytes((uint)tmp19.Key.Count()));
						while (tmp20.Count > 0 && tmp20.Last() == 0)
							tmp20.RemoveAt(tmp20.Count - 1);
						s.Add((byte)tmp20.Count);
						s.AddRange(tmp20);
						
						s.AddRange(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(tmp19.Key));
					}
					
					s.Add((byte)((tmp19.Value == null) ? 0 : 1));
					if (tmp19.Value != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp19.Value));
					}
				}
			}
			
			// serialize Pacman
			s.Add((byte)((Pacman == null) ? 0 : 1));
			if (Pacman != null)
			{
				s.AddRange(Pacman.Serialize());
			}
			
			// serialize Ghosts
			s.Add((byte)((Ghosts == null) ? 0 : 1));
			if (Ghosts != null)
			{
				List<byte> tmp21 = new List<byte>();
				tmp21.AddRange(BitConverter.GetBytes((uint)Ghosts.Count()));
				while (tmp21.Count > 0 && tmp21.Last() == 0)
					tmp21.RemoveAt(tmp21.Count - 1);
				s.Add((byte)tmp21.Count);
				s.AddRange(tmp21);
				
				foreach (var tmp22 in Ghosts)
				{
					s.Add((byte)((tmp22 == null) ? 0 : 1));
					if (tmp22 != null)
					{
						s.AddRange(tmp22.Serialize());
					}
				}
			}
			
			// serialize Constants
			s.Add((byte)((Constants == null) ? 0 : 1));
			if (Constants != null)
			{
				s.AddRange(Constants.Serialize());
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Width
			byte tmp23;
			tmp23 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp23 == 1)
			{
				Width = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Width = null;
			
			// deserialize Height
			byte tmp24;
			tmp24 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp24 == 1)
			{
				Height = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Height = null;
			
			// deserialize Board
			byte tmp25;
			tmp25 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp25 == 1)
			{
				byte tmp26;
				tmp26 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp27 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp27, 0, tmp26);
				offset += tmp26;
				uint tmp28;
				tmp28 = BitConverter.ToUInt32(tmp27, (int)0);
				
				Board = new List<List<ECell?>>();
				for (uint tmp29 = 0; tmp29 < tmp28; tmp29++)
				{
					List<ECell?> tmp30;
					byte tmp31;
					tmp31 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp31 == 1)
					{
						byte tmp32;
						tmp32 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp33 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp33, 0, tmp32);
						offset += tmp32;
						uint tmp34;
						tmp34 = BitConverter.ToUInt32(tmp33, (int)0);
						
						tmp30 = new List<ECell?>();
						for (uint tmp35 = 0; tmp35 < tmp34; tmp35++)
						{
							ECell? tmp36;
							byte tmp37;
							tmp37 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp37 == 1)
							{
								sbyte tmp38;
								tmp38 = (sbyte)s[(int)offset];
								offset += sizeof(sbyte);
								tmp36 = (ECell)tmp38;
							}
							else
								tmp36 = null;
							tmp30.Add(tmp36);
						}
					}
					else
						tmp30 = null;
					Board.Add(tmp30);
				}
			}
			else
				Board = null;
			
			// deserialize Scores
			byte tmp39;
			tmp39 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp39 == 1)
			{
				byte tmp40;
				tmp40 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp41 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp41, 0, tmp40);
				offset += tmp40;
				uint tmp42;
				tmp42 = BitConverter.ToUInt32(tmp41, (int)0);
				
				Scores = new Dictionary<string, int?>();
				for (uint tmp43 = 0; tmp43 < tmp42; tmp43++)
				{
					string tmp44;
					byte tmp46;
					tmp46 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp46 == 1)
					{
						byte tmp47;
						tmp47 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp48 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp48, 0, tmp47);
						offset += tmp47;
						uint tmp49;
						tmp49 = BitConverter.ToUInt32(tmp48, (int)0);
						
						tmp44 = System.Text.Encoding.GetEncoding("ISO-8859-1").GetString(s.Skip((int)offset).Take((int)tmp49).ToArray());
						offset += tmp49;
					}
					else
						tmp44 = null;
					
					int? tmp45;
					byte tmp50;
					tmp50 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp50 == 1)
					{
						tmp45 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp45 = null;
					
					Scores[tmp44] = tmp45;
				}
			}
			else
				Scores = null;
			
			// deserialize Pacman
			byte tmp51;
			tmp51 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp51 == 1)
			{
				Pacman = new Pacman();
				offset = Pacman.Deserialize(s, offset);
			}
			else
				Pacman = null;
			
			// deserialize Ghosts
			byte tmp52;
			tmp52 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp52 == 1)
			{
				byte tmp53;
				tmp53 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp54 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp54, 0, tmp53);
				offset += tmp53;
				uint tmp55;
				tmp55 = BitConverter.ToUInt32(tmp54, (int)0);
				
				Ghosts = new List<Ghost>();
				for (uint tmp56 = 0; tmp56 < tmp55; tmp56++)
				{
					Ghost tmp57;
					byte tmp58;
					tmp58 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp58 == 1)
					{
						tmp57 = new Ghost();
						offset = tmp57.Deserialize(s, offset);
					}
					else
						tmp57 = null;
					Ghosts.Add(tmp57);
				}
			}
			else
				Ghosts = null;
			
			// deserialize Constants
			byte tmp59;
			tmp59 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp59 == 1)
			{
				Constants = new Constants();
				offset = Constants.Deserialize(s, offset);
			}
			else
				Constants = null;
			
			return offset;
		}
	}
} // namespace KS.Models
