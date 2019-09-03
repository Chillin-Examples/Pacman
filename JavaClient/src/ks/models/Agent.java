package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Agent extends KSObject
{
	protected Position position;
	protected EDirection direction;
	
	// getters
	
	public Position getPosition()
	{
		return this.position;
	}
	
	public EDirection getDirection()
	{
		return this.direction;
	}
	
	
	// setters
	
	public void setPosition(Position position)
	{
		this.position = position;
	}
	
	public void setDirection(EDirection direction)
	{
		this.direction = direction;
	}
	
	
	public Agent()
	{
	}
	
	public static final String nameStatic = "Agent";
	
	@Override
	public String name() { return "Agent"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize position
		s.add((byte) ((position == null) ? 0 : 1));
		if (position != null)
		{
			s.addAll(b2B(position.serialize()));
		}
		
		// serialize direction
		s.add((byte) ((direction == null) ? 0 : 1));
		if (direction != null)
		{
			s.add((byte) (direction.getValue()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize position
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			position = new Position();
			offset = position.deserialize(s, offset);
		}
		else
			position = null;
		
		// deserialize direction
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			byte tmp2;
			tmp2 = s[offset];
			offset += Byte.BYTES;
			direction = EDirection.of(tmp2);
		}
		else
			direction = null;
		
		return offset;
	}
}
