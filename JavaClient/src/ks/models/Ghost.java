package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Ghost extends Agent
{
	protected Integer id;
	
	// getters
	
	public Integer getId()
	{
		return this.id;
	}
	
	
	// setters
	
	public void setId(Integer id)
	{
		this.id = id;
	}
	
	
	public Ghost()
	{
	}
	
	public static final String nameStatic = "Ghost";
	
	@Override
	public String name() { return "Ghost"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize parents
		s.addAll(b2B(super.serialize()));
		
		// serialize id
		s.add((byte) ((id == null) ? 0 : 1));
		if (id != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(id).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize parents
		offset = super.deserialize(s, offset);
		
		// deserialize id
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			id = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			id = null;
		
		return offset;
	}
}
