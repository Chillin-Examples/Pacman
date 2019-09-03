package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Constants extends KSObject
{
	protected Integer foodScore;
	protected Integer superFoodScore;
	protected Integer ghostDeathScore;
	protected Integer pacmanDeathScore;
	protected Integer pacmanGiantFormDuration;
	protected Integer maxCycles;
	
	// getters
	
	public Integer getFoodScore()
	{
		return this.foodScore;
	}
	
	public Integer getSuperFoodScore()
	{
		return this.superFoodScore;
	}
	
	public Integer getGhostDeathScore()
	{
		return this.ghostDeathScore;
	}
	
	public Integer getPacmanDeathScore()
	{
		return this.pacmanDeathScore;
	}
	
	public Integer getPacmanGiantFormDuration()
	{
		return this.pacmanGiantFormDuration;
	}
	
	public Integer getMaxCycles()
	{
		return this.maxCycles;
	}
	
	
	// setters
	
	public void setFoodScore(Integer foodScore)
	{
		this.foodScore = foodScore;
	}
	
	public void setSuperFoodScore(Integer superFoodScore)
	{
		this.superFoodScore = superFoodScore;
	}
	
	public void setGhostDeathScore(Integer ghostDeathScore)
	{
		this.ghostDeathScore = ghostDeathScore;
	}
	
	public void setPacmanDeathScore(Integer pacmanDeathScore)
	{
		this.pacmanDeathScore = pacmanDeathScore;
	}
	
	public void setPacmanGiantFormDuration(Integer pacmanGiantFormDuration)
	{
		this.pacmanGiantFormDuration = pacmanGiantFormDuration;
	}
	
	public void setMaxCycles(Integer maxCycles)
	{
		this.maxCycles = maxCycles;
	}
	
	
	public Constants()
	{
	}
	
	public static final String nameStatic = "Constants";
	
	@Override
	public String name() { return "Constants"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize foodScore
		s.add((byte) ((foodScore == null) ? 0 : 1));
		if (foodScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(foodScore).array()));
		}
		
		// serialize superFoodScore
		s.add((byte) ((superFoodScore == null) ? 0 : 1));
		if (superFoodScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(superFoodScore).array()));
		}
		
		// serialize ghostDeathScore
		s.add((byte) ((ghostDeathScore == null) ? 0 : 1));
		if (ghostDeathScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(ghostDeathScore).array()));
		}
		
		// serialize pacmanDeathScore
		s.add((byte) ((pacmanDeathScore == null) ? 0 : 1));
		if (pacmanDeathScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(pacmanDeathScore).array()));
		}
		
		// serialize pacmanGiantFormDuration
		s.add((byte) ((pacmanGiantFormDuration == null) ? 0 : 1));
		if (pacmanGiantFormDuration != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(pacmanGiantFormDuration).array()));
		}
		
		// serialize maxCycles
		s.add((byte) ((maxCycles == null) ? 0 : 1));
		if (maxCycles != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(maxCycles).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize foodScore
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			foodScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			foodScore = null;
		
		// deserialize superFoodScore
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			superFoodScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			superFoodScore = null;
		
		// deserialize ghostDeathScore
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			ghostDeathScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			ghostDeathScore = null;
		
		// deserialize pacmanDeathScore
		byte tmp3;
		tmp3 = s[offset];
		offset += Byte.BYTES;
		if (tmp3 == 1)
		{
			pacmanDeathScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			pacmanDeathScore = null;
		
		// deserialize pacmanGiantFormDuration
		byte tmp4;
		tmp4 = s[offset];
		offset += Byte.BYTES;
		if (tmp4 == 1)
		{
			pacmanGiantFormDuration = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			pacmanGiantFormDuration = null;
		
		// deserialize maxCycles
		byte tmp5;
		tmp5 = s[offset];
		offset += Byte.BYTES;
		if (tmp5 == 1)
		{
			maxCycles = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			maxCycles = null;
		
		return offset;
	}
}
