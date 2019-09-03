package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Pacman extends Agent
{
	protected Integer health;
	protected Integer giantFormRemainingTime;
	
	// getters
	
	public Integer getHealth()
	{
		return this.health;
	}
	
	public Integer getGiantFormRemainingTime()
	{
		return this.giantFormRemainingTime;
	}
	
	
	// setters
	
	public void setHealth(Integer health)
	{
		this.health = health;
	}
	
	public void setGiantFormRemainingTime(Integer giantFormRemainingTime)
	{
		this.giantFormRemainingTime = giantFormRemainingTime;
	}
	
	
	public Pacman()
	{
	}
	
	public static final String nameStatic = "Pacman";
	
	@Override
	public String name() { return "Pacman"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize parents
		s.addAll(b2B(super.serialize()));
		
		// serialize health
		s.add((byte) ((health == null) ? 0 : 1));
		if (health != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(health).array()));
		}
		
		// serialize giantFormRemainingTime
		s.add((byte) ((giantFormRemainingTime == null) ? 0 : 1));
		if (giantFormRemainingTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(giantFormRemainingTime).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize parents
		offset = super.deserialize(s, offset);
		
		// deserialize health
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			health = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			health = null;
		
		// deserialize giantFormRemainingTime
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			giantFormRemainingTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			giantFormRemainingTime = null;
		
		return offset;
	}
}
