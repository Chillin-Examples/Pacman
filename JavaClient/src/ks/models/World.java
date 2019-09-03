package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class World extends KSObject
{
	protected Integer width;
	protected Integer height;
	protected List<List<ECell>> board;
	protected Map<String, Integer> scores;
	protected Pacman pacman;
	protected List<Ghost> ghosts;
	protected Constants constants;
	
	// getters
	
	public Integer getWidth()
	{
		return this.width;
	}
	
	public Integer getHeight()
	{
		return this.height;
	}
	
	public List<List<ECell>> getBoard()
	{
		return this.board;
	}
	
	public Map<String, Integer> getScores()
	{
		return this.scores;
	}
	
	public Pacman getPacman()
	{
		return this.pacman;
	}
	
	public List<Ghost> getGhosts()
	{
		return this.ghosts;
	}
	
	public Constants getConstants()
	{
		return this.constants;
	}
	
	
	// setters
	
	public void setWidth(Integer width)
	{
		this.width = width;
	}
	
	public void setHeight(Integer height)
	{
		this.height = height;
	}
	
	public void setBoard(List<List<ECell>> board)
	{
		this.board = board;
	}
	
	public void setScores(Map<String, Integer> scores)
	{
		this.scores = scores;
	}
	
	public void setPacman(Pacman pacman)
	{
		this.pacman = pacman;
	}
	
	public void setGhosts(List<Ghost> ghosts)
	{
		this.ghosts = ghosts;
	}
	
	public void setConstants(Constants constants)
	{
		this.constants = constants;
	}
	
	
	public World()
	{
	}
	
	public static final String nameStatic = "World";
	
	@Override
	public String name() { return "World"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize width
		s.add((byte) ((width == null) ? 0 : 1));
		if (width != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(width).array()));
		}
		
		// serialize height
		s.add((byte) ((height == null) ? 0 : 1));
		if (height != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(height).array()));
		}
		
		// serialize board
		s.add((byte) ((board == null) ? 0 : 1));
		if (board != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(board.size()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			for (List<ECell> tmp1 : board)
			{
				s.add((byte) ((tmp1 == null) ? 0 : 1));
				if (tmp1 != null)
				{
					List<Byte> tmp2 = new ArrayList<>();
					tmp2.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp1.size()).array()));
					while (tmp2.size() > 0 && tmp2.get(tmp2.size() - 1) == 0)
						tmp2.remove(tmp2.size() - 1);
					s.add((byte) tmp2.size());
					s.addAll(tmp2);
					
					for (ECell tmp3 : tmp1)
					{
						s.add((byte) ((tmp3 == null) ? 0 : 1));
						if (tmp3 != null)
						{
							s.add((byte) (tmp3.getValue()));
						}
					}
				}
			}
		}
		
		// serialize scores
		s.add((byte) ((scores == null) ? 0 : 1));
		if (scores != null)
		{
			List<Byte> tmp4 = new ArrayList<>();
			tmp4.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(scores.size()).array()));
			while (tmp4.size() > 0 && tmp4.get(tmp4.size() - 1) == 0)
				tmp4.remove(tmp4.size() - 1);
			s.add((byte) tmp4.size());
			s.addAll(tmp4);
			
			for (Map.Entry<String, Integer> tmp5 : scores.entrySet())
			{
				s.add((byte) ((tmp5.getKey() == null) ? 0 : 1));
				if (tmp5.getKey() != null)
				{
					List<Byte> tmp6 = new ArrayList<>();
					tmp6.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp5.getKey().length()).array()));
					while (tmp6.size() > 0 && tmp6.get(tmp6.size() - 1) == 0)
						tmp6.remove(tmp6.size() - 1);
					s.add((byte) tmp6.size());
					s.addAll(tmp6);
					
					s.addAll(b2B(tmp5.getKey().getBytes(Charset.forName("ISO-8859-1"))));
				}
				
				s.add((byte) ((tmp5.getValue() == null) ? 0 : 1));
				if (tmp5.getValue() != null)
				{
					s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp5.getValue()).array()));
				}
			}
		}
		
		// serialize pacman
		s.add((byte) ((pacman == null) ? 0 : 1));
		if (pacman != null)
		{
			s.addAll(b2B(pacman.serialize()));
		}
		
		// serialize ghosts
		s.add((byte) ((ghosts == null) ? 0 : 1));
		if (ghosts != null)
		{
			List<Byte> tmp7 = new ArrayList<>();
			tmp7.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(ghosts.size()).array()));
			while (tmp7.size() > 0 && tmp7.get(tmp7.size() - 1) == 0)
				tmp7.remove(tmp7.size() - 1);
			s.add((byte) tmp7.size());
			s.addAll(tmp7);
			
			for (Ghost tmp8 : ghosts)
			{
				s.add((byte) ((tmp8 == null) ? 0 : 1));
				if (tmp8 != null)
				{
					s.addAll(b2B(tmp8.serialize()));
				}
			}
		}
		
		// serialize constants
		s.add((byte) ((constants == null) ? 0 : 1));
		if (constants != null)
		{
			s.addAll(b2B(constants.serialize()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize width
		byte tmp9;
		tmp9 = s[offset];
		offset += Byte.BYTES;
		if (tmp9 == 1)
		{
			width = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			width = null;
		
		// deserialize height
		byte tmp10;
		tmp10 = s[offset];
		offset += Byte.BYTES;
		if (tmp10 == 1)
		{
			height = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			height = null;
		
		// deserialize board
		byte tmp11;
		tmp11 = s[offset];
		offset += Byte.BYTES;
		if (tmp11 == 1)
		{
			byte tmp12;
			tmp12 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp13 = Arrays.copyOfRange(s, offset, offset + tmp12);
			offset += tmp12;
			int tmp14;
			tmp14 = ByteBuffer.wrap(Arrays.copyOfRange(tmp13, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			board = new ArrayList<>();
			for (int tmp15 = 0; tmp15 < tmp14; tmp15++)
			{
				List<ECell> tmp16;
				byte tmp17;
				tmp17 = s[offset];
				offset += Byte.BYTES;
				if (tmp17 == 1)
				{
					byte tmp18;
					tmp18 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp19 = Arrays.copyOfRange(s, offset, offset + tmp18);
					offset += tmp18;
					int tmp20;
					tmp20 = ByteBuffer.wrap(Arrays.copyOfRange(tmp19, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp16 = new ArrayList<>();
					for (int tmp21 = 0; tmp21 < tmp20; tmp21++)
					{
						ECell tmp22;
						byte tmp23;
						tmp23 = s[offset];
						offset += Byte.BYTES;
						if (tmp23 == 1)
						{
							byte tmp24;
							tmp24 = s[offset];
							offset += Byte.BYTES;
							tmp22 = ECell.of(tmp24);
						}
						else
							tmp22 = null;
						tmp16.add(tmp22);
					}
				}
				else
					tmp16 = null;
				board.add(tmp16);
			}
		}
		else
			board = null;
		
		// deserialize scores
		byte tmp25;
		tmp25 = s[offset];
		offset += Byte.BYTES;
		if (tmp25 == 1)
		{
			byte tmp26;
			tmp26 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp27 = Arrays.copyOfRange(s, offset, offset + tmp26);
			offset += tmp26;
			int tmp28;
			tmp28 = ByteBuffer.wrap(Arrays.copyOfRange(tmp27, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			scores = new HashMap<>();
			for (int tmp29 = 0; tmp29 < tmp28; tmp29++)
			{
				String tmp30;
				byte tmp32;
				tmp32 = s[offset];
				offset += Byte.BYTES;
				if (tmp32 == 1)
				{
					byte tmp33;
					tmp33 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp34 = Arrays.copyOfRange(s, offset, offset + tmp33);
					offset += tmp33;
					int tmp35;
					tmp35 = ByteBuffer.wrap(Arrays.copyOfRange(tmp34, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp30 = new String(s, offset, tmp35, Charset.forName("ISO-8859-1"));
					offset += tmp35;
				}
				else
					tmp30 = null;
				
				Integer tmp31;
				byte tmp36;
				tmp36 = s[offset];
				offset += Byte.BYTES;
				if (tmp36 == 1)
				{
					tmp31 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					offset += Integer.BYTES;
				}
				else
					tmp31 = null;
				
				scores.put(tmp30, tmp31);
			}
		}
		else
			scores = null;
		
		// deserialize pacman
		byte tmp37;
		tmp37 = s[offset];
		offset += Byte.BYTES;
		if (tmp37 == 1)
		{
			pacman = new Pacman();
			offset = pacman.deserialize(s, offset);
		}
		else
			pacman = null;
		
		// deserialize ghosts
		byte tmp38;
		tmp38 = s[offset];
		offset += Byte.BYTES;
		if (tmp38 == 1)
		{
			byte tmp39;
			tmp39 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp40 = Arrays.copyOfRange(s, offset, offset + tmp39);
			offset += tmp39;
			int tmp41;
			tmp41 = ByteBuffer.wrap(Arrays.copyOfRange(tmp40, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			ghosts = new ArrayList<>();
			for (int tmp42 = 0; tmp42 < tmp41; tmp42++)
			{
				Ghost tmp43;
				byte tmp44;
				tmp44 = s[offset];
				offset += Byte.BYTES;
				if (tmp44 == 1)
				{
					tmp43 = new Ghost();
					offset = tmp43.deserialize(s, offset);
				}
				else
					tmp43 = null;
				ghosts.add(tmp43);
			}
		}
		else
			ghosts = null;
		
		// deserialize constants
		byte tmp45;
		tmp45 = s[offset];
		offset += Byte.BYTES;
		if (tmp45 == 1)
		{
			constants = new Constants();
			offset = constants.deserialize(s, offset);
		}
		else
			constants = null;
		
		return offset;
	}
}
