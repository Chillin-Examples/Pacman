using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Commands
{
	public enum ECommandDirection
	{
		Up = 0,
		Right = 1,
		Down = 2,
		Left = 3,
	}
	
	public partial class ChangePacmanDirection : KSObject
	{
		public ECommandDirection? Direction { get; set; }
		

		public ChangePacmanDirection()
		{
		}
		
		public new const string NameStatic = "ChangePacmanDirection";
		
		public override string Name() => "ChangePacmanDirection";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
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
			// deserialize Direction
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				sbyte tmp1;
				tmp1 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (ECommandDirection)tmp1;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
	
	public partial class ChangeGhostDirection : KSObject
	{
		public int? Id { get; set; }
		public ECommandDirection? Direction { get; set; }
		

		public ChangeGhostDirection()
		{
		}
		
		public new const string NameStatic = "ChangeGhostDirection";
		
		public override string Name() => "ChangeGhostDirection";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
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
			// deserialize Id
			byte tmp2;
			tmp2 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp2 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Direction
			byte tmp3;
			tmp3 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp3 == 1)
			{
				sbyte tmp4;
				tmp4 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (ECommandDirection)tmp4;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
} // namespace KS.Commands
