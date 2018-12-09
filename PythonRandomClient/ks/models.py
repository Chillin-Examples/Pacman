# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECell(Enum):
	Empty = 0
	Food = 1
	SuperFood = 2
	Wall = 3


class EDirection(Enum):
	Up = 0
	Right = 1
	Down = 2
	Left = 3


class Constants(object):

	@staticmethod
	def name():
		return 'Constants'


	def __init__(self, food_score=None, super_food_score=None, ghost_death_score=None, pacman_death_score=None, pacman_giant_form_duration=None, max_cycles=None):
		self.initialize(food_score, super_food_score, ghost_death_score, pacman_death_score, pacman_giant_form_duration, max_cycles)
	

	def initialize(self, food_score=None, super_food_score=None, ghost_death_score=None, pacman_death_score=None, pacman_giant_form_duration=None, max_cycles=None):
		self.food_score = food_score
		self.super_food_score = super_food_score
		self.ghost_death_score = ghost_death_score
		self.pacman_death_score = pacman_death_score
		self.pacman_giant_form_duration = pacman_giant_form_duration
		self.max_cycles = max_cycles
	

	def serialize(self):
		s = b''
		
		# serialize self.food_score
		s += b'\x00' if self.food_score is None else b'\x01'
		if self.food_score is not None:
			s += struct.pack('i', self.food_score)
		
		# serialize self.super_food_score
		s += b'\x00' if self.super_food_score is None else b'\x01'
		if self.super_food_score is not None:
			s += struct.pack('i', self.super_food_score)
		
		# serialize self.ghost_death_score
		s += b'\x00' if self.ghost_death_score is None else b'\x01'
		if self.ghost_death_score is not None:
			s += struct.pack('i', self.ghost_death_score)
		
		# serialize self.pacman_death_score
		s += b'\x00' if self.pacman_death_score is None else b'\x01'
		if self.pacman_death_score is not None:
			s += struct.pack('i', self.pacman_death_score)
		
		# serialize self.pacman_giant_form_duration
		s += b'\x00' if self.pacman_giant_form_duration is None else b'\x01'
		if self.pacman_giant_form_duration is not None:
			s += struct.pack('i', self.pacman_giant_form_duration)
		
		# serialize self.max_cycles
		s += b'\x00' if self.max_cycles is None else b'\x01'
		if self.max_cycles is not None:
			s += struct.pack('i', self.max_cycles)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.food_score
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.food_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.food_score = None
		
		# deserialize self.super_food_score
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.super_food_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.super_food_score = None
		
		# deserialize self.ghost_death_score
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.ghost_death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.ghost_death_score = None
		
		# deserialize self.pacman_death_score
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.pacman_death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.pacman_death_score = None
		
		# deserialize self.pacman_giant_form_duration
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.pacman_giant_form_duration = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.pacman_giant_form_duration = None
		
		# deserialize self.max_cycles
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.max_cycles = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_cycles = None
		
		return offset


class Pacman(object):

	@staticmethod
	def name():
		return 'Pacman'


	def __init__(self, x=None, y=None, direction=None, health=None, giant_form_remaining_time=None, init_x=None, init_y=None, init_direction=None):
		self.initialize(x, y, direction, health, giant_form_remaining_time, init_x, init_y, init_direction)
	

	def initialize(self, x=None, y=None, direction=None, health=None, giant_form_remaining_time=None, init_x=None, init_y=None, init_direction=None):
		self.x = x
		self.y = y
		self.direction = direction
		self.health = health
		self.giant_form_remaining_time = giant_form_remaining_time
		self.init_x = init_x
		self.init_y = init_y
		self.init_direction = init_direction
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('i', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('i', self.y)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		# serialize self.health
		s += b'\x00' if self.health is None else b'\x01'
		if self.health is not None:
			s += struct.pack('i', self.health)
		
		# serialize self.giant_form_remaining_time
		s += b'\x00' if self.giant_form_remaining_time is None else b'\x01'
		if self.giant_form_remaining_time is not None:
			s += struct.pack('i', self.giant_form_remaining_time)
		
		# serialize self.init_x
		s += b'\x00' if self.init_x is None else b'\x01'
		if self.init_x is not None:
			s += struct.pack('i', self.init_x)
		
		# serialize self.init_y
		s += b'\x00' if self.init_y is None else b'\x01'
		if self.init_y is not None:
			s += struct.pack('i', self.init_y)
		
		# serialize self.init_direction
		s += b'\x00' if self.init_direction is None else b'\x01'
		if self.init_direction is not None:
			s += struct.pack('b', self.init_direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.direction
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			tmp9 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp9)
		else:
			self.direction = None
		
		# deserialize self.health
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.giant_form_remaining_time
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.giant_form_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.giant_form_remaining_time = None
		
		# deserialize self.init_x
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.init_x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.init_x = None
		
		# deserialize self.init_y
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.init_y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.init_y = None
		
		# deserialize self.init_direction
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			tmp15 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.init_direction = EDirection(tmp15)
		else:
			self.init_direction = None
		
		return offset


class Ghost(object):

	@staticmethod
	def name():
		return 'Ghost'


	def __init__(self, x=None, y=None, id=None, direction=None, init_x=None, init_y=None, init_direction=None):
		self.initialize(x, y, id, direction, init_x, init_y, init_direction)
	

	def initialize(self, x=None, y=None, id=None, direction=None, init_x=None, init_y=None, init_direction=None):
		self.x = x
		self.y = y
		self.id = id
		self.direction = direction
		self.init_x = init_x
		self.init_y = init_y
		self.init_direction = init_direction
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('i', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('i', self.y)
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		# serialize self.init_x
		s += b'\x00' if self.init_x is None else b'\x01'
		if self.init_x is not None:
			s += struct.pack('i', self.init_x)
		
		# serialize self.init_y
		s += b'\x00' if self.init_y is None else b'\x01'
		if self.init_y is not None:
			s += struct.pack('i', self.init_y)
		
		# serialize self.init_direction
		s += b'\x00' if self.init_direction is None else b'\x01'
		if self.init_direction is not None:
			s += struct.pack('b', self.init_direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp17:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.id
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			tmp20 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp20)
		else:
			self.direction = None
		
		# deserialize self.init_x
		tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp21:
			self.init_x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.init_x = None
		
		# deserialize self.init_y
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			self.init_y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.init_y = None
		
		# deserialize self.init_direction
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			tmp24 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.init_direction = EDirection(tmp24)
		else:
			self.init_direction = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, width=None, height=None, board=None, scores=None, pacman=None, ghosts=None, constants=None):
		self.initialize(width, height, board, scores, pacman, ghosts, constants)
	

	def initialize(self, width=None, height=None, board=None, scores=None, pacman=None, ghosts=None, constants=None):
		self.width = width
		self.height = height
		self.board = board
		self.scores = scores
		self.pacman = pacman
		self.ghosts = ghosts
		self.constants = constants
	

	def serialize(self):
		s = b''
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('i', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('i', self.height)
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp25 = b''
			tmp25 += struct.pack('I', len(self.board))
			while len(tmp25) and tmp25[-1] == b'\x00'[0]:
				tmp25 = tmp25[:-1]
			s += struct.pack('B', len(tmp25))
			s += tmp25
			
			for tmp26 in self.board:
				s += b'\x00' if tmp26 is None else b'\x01'
				if tmp26 is not None:
					tmp27 = b''
					tmp27 += struct.pack('I', len(tmp26))
					while len(tmp27) and tmp27[-1] == b'\x00'[0]:
						tmp27 = tmp27[:-1]
					s += struct.pack('B', len(tmp27))
					s += tmp27
					
					for tmp28 in tmp26:
						s += b'\x00' if tmp28 is None else b'\x01'
						if tmp28 is not None:
							s += struct.pack('b', tmp28.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp29 = b''
			tmp29 += struct.pack('I', len(self.scores))
			while len(tmp29) and tmp29[-1] == b'\x00'[0]:
				tmp29 = tmp29[:-1]
			s += struct.pack('B', len(tmp29))
			s += tmp29
			
			for tmp30 in self.scores:
				s += b'\x00' if tmp30 is None else b'\x01'
				if tmp30 is not None:
					tmp31 = b''
					tmp31 += struct.pack('I', len(tmp30))
					while len(tmp31) and tmp31[-1] == b'\x00'[0]:
						tmp31 = tmp31[:-1]
					s += struct.pack('B', len(tmp31))
					s += tmp31
					
					s += tmp30.encode('ISO-8859-1') if PY3 else tmp30
				s += b'\x00' if self.scores[tmp30] is None else b'\x01'
				if self.scores[tmp30] is not None:
					s += struct.pack('i', self.scores[tmp30])
		
		# serialize self.pacman
		s += b'\x00' if self.pacman is None else b'\x01'
		if self.pacman is not None:
			s += self.pacman.serialize()
		
		# serialize self.ghosts
		s += b'\x00' if self.ghosts is None else b'\x01'
		if self.ghosts is not None:
			tmp32 = b''
			tmp32 += struct.pack('I', len(self.ghosts))
			while len(tmp32) and tmp32[-1] == b'\x00'[0]:
				tmp32 = tmp32[:-1]
			s += struct.pack('B', len(tmp32))
			s += tmp32
			
			for tmp33 in self.ghosts:
				s += b'\x00' if tmp33 is None else b'\x01'
				if tmp33 is not None:
					s += tmp33.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp38 = s[offset:offset + tmp37]
			offset += tmp37
			tmp38 += b'\x00' * (4 - tmp37)
			tmp39 = struct.unpack('I', tmp38)[0]
			
			self.board = []
			for tmp40 in range(tmp39):
				tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp42:
					tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp44 = s[offset:offset + tmp43]
					offset += tmp43
					tmp44 += b'\x00' * (4 - tmp43)
					tmp45 = struct.unpack('I', tmp44)[0]
					
					tmp41 = []
					for tmp46 in range(tmp45):
						tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp48:
							tmp49 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp47 = ECell(tmp49)
						else:
							tmp47 = None
						tmp41.append(tmp47)
				else:
					tmp41 = None
				self.board.append(tmp41)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp52 = s[offset:offset + tmp51]
			offset += tmp51
			tmp52 += b'\x00' * (4 - tmp51)
			tmp53 = struct.unpack('I', tmp52)[0]
			
			self.scores = {}
			for tmp54 in range(tmp53):
				tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp57:
					tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp59 = s[offset:offset + tmp58]
					offset += tmp58
					tmp59 += b'\x00' * (4 - tmp58)
					tmp60 = struct.unpack('I', tmp59)[0]
					
					tmp55 = s[offset:offset + tmp60].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp60]
					offset += tmp60
				else:
					tmp55 = None
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp56 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp56 = None
				self.scores[tmp55] = tmp56
		else:
			self.scores = None
		
		# deserialize self.pacman
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			self.pacman = Pacman()
			offset = self.pacman.deserialize(s, offset)
		else:
			self.pacman = None
		
		# deserialize self.ghosts
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp65 = s[offset:offset + tmp64]
			offset += tmp64
			tmp65 += b'\x00' * (4 - tmp64)
			tmp66 = struct.unpack('I', tmp65)[0]
			
			self.ghosts = []
			for tmp67 in range(tmp66):
				tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp69:
					tmp68 = Ghost()
					offset = tmp68.deserialize(s, offset)
				else:
					tmp68 = None
				self.ghosts.append(tmp68)
		else:
			self.ghosts = None
		
		# deserialize self.constants
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
