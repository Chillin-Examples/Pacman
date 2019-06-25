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


class Position(object):

	@staticmethod
	def name():
		return 'Position'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

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
		
		return offset


class Agent(object):

	@staticmethod
	def name():
		return 'Agent'


	def __init__(self, position=None, direction=None):
		self.initialize(position, direction)
	

	def initialize(self, position=None, direction=None):
		self.position = position
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.position
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.direction
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			tmp10 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp10)
		else:
			self.direction = None
		
		return offset


class Pacman(Agent):

	@staticmethod
	def name():
		return 'Pacman'


	def __init__(self, position=None, direction=None, health=None, giant_form_remaining_time=None):
		self.initialize(position, direction, health, giant_form_remaining_time)
	

	def initialize(self, position=None, direction=None, health=None, giant_form_remaining_time=None):
		Agent.initialize(self, position, direction)
		
		self.health = health
		self.giant_form_remaining_time = giant_form_remaining_time
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Agent.serialize(self)
		
		# serialize self.health
		s += b'\x00' if self.health is None else b'\x01'
		if self.health is not None:
			s += struct.pack('i', self.health)
		
		# serialize self.giant_form_remaining_time
		s += b'\x00' if self.giant_form_remaining_time is None else b'\x01'
		if self.giant_form_remaining_time is not None:
			s += struct.pack('i', self.giant_form_remaining_time)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Agent.deserialize(self, s, offset)
		
		# deserialize self.health
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.giant_form_remaining_time
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.giant_form_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.giant_form_remaining_time = None
		
		return offset


class Ghost(Agent):

	@staticmethod
	def name():
		return 'Ghost'


	def __init__(self, position=None, direction=None, id=None):
		self.initialize(position, direction, id)
	

	def initialize(self, position=None, direction=None, id=None):
		Agent.initialize(self, position, direction)
		
		self.id = id
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Agent.serialize(self)
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Agent.deserialize(self, s, offset)
		
		# deserialize self.id
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
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
			tmp14 = b''
			tmp14 += struct.pack('I', len(self.board))
			while len(tmp14) and tmp14[-1] == b'\x00'[0]:
				tmp14 = tmp14[:-1]
			s += struct.pack('B', len(tmp14))
			s += tmp14
			
			for tmp15 in self.board:
				s += b'\x00' if tmp15 is None else b'\x01'
				if tmp15 is not None:
					tmp16 = b''
					tmp16 += struct.pack('I', len(tmp15))
					while len(tmp16) and tmp16[-1] == b'\x00'[0]:
						tmp16 = tmp16[:-1]
					s += struct.pack('B', len(tmp16))
					s += tmp16
					
					for tmp17 in tmp15:
						s += b'\x00' if tmp17 is None else b'\x01'
						if tmp17 is not None:
							s += struct.pack('b', tmp17.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.scores))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			for tmp19 in self.scores:
				s += b'\x00' if tmp19 is None else b'\x01'
				if tmp19 is not None:
					tmp20 = b''
					tmp20 += struct.pack('I', len(tmp19))
					while len(tmp20) and tmp20[-1] == b'\x00'[0]:
						tmp20 = tmp20[:-1]
					s += struct.pack('B', len(tmp20))
					s += tmp20
					
					s += tmp19.encode('ISO-8859-1') if PY3 else tmp19
				s += b'\x00' if self.scores[tmp19] is None else b'\x01'
				if self.scores[tmp19] is not None:
					s += struct.pack('i', self.scores[tmp19])
		
		# serialize self.pacman
		s += b'\x00' if self.pacman is None else b'\x01'
		if self.pacman is not None:
			s += self.pacman.serialize()
		
		# serialize self.ghosts
		s += b'\x00' if self.ghosts is None else b'\x01'
		if self.ghosts is not None:
			tmp21 = b''
			tmp21 += struct.pack('I', len(self.ghosts))
			while len(tmp21) and tmp21[-1] == b'\x00'[0]:
				tmp21 = tmp21[:-1]
			s += struct.pack('B', len(tmp21))
			s += tmp21
			
			for tmp22 in self.ghosts:
				s += b'\x00' if tmp22 is None else b'\x01'
				if tmp22 is not None:
					s += tmp22.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
			tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp27 = s[offset:offset + tmp26]
			offset += tmp26
			tmp27 += b'\x00' * (4 - tmp26)
			tmp28 = struct.unpack('I', tmp27)[0]
			
			self.board = []
			for tmp29 in range(tmp28):
				tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp31:
					tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp33 = s[offset:offset + tmp32]
					offset += tmp32
					tmp33 += b'\x00' * (4 - tmp32)
					tmp34 = struct.unpack('I', tmp33)[0]
					
					tmp30 = []
					for tmp35 in range(tmp34):
						tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp37:
							tmp38 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp36 = ECell(tmp38)
						else:
							tmp36 = None
						tmp30.append(tmp36)
				else:
					tmp30 = None
				self.board.append(tmp30)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp41 = s[offset:offset + tmp40]
			offset += tmp40
			tmp41 += b'\x00' * (4 - tmp40)
			tmp42 = struct.unpack('I', tmp41)[0]
			
			self.scores = {}
			for tmp43 in range(tmp42):
				tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp46:
					tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp48 = s[offset:offset + tmp47]
					offset += tmp47
					tmp48 += b'\x00' * (4 - tmp47)
					tmp49 = struct.unpack('I', tmp48)[0]
					
					tmp44 = s[offset:offset + tmp49].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp49]
					offset += tmp49
				else:
					tmp44 = None
				tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp50:
					tmp45 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp45 = None
				self.scores[tmp44] = tmp45
		else:
			self.scores = None
		
		# deserialize self.pacman
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.pacman = Pacman()
			offset = self.pacman.deserialize(s, offset)
		else:
			self.pacman = None
		
		# deserialize self.ghosts
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp54 = s[offset:offset + tmp53]
			offset += tmp53
			tmp54 += b'\x00' * (4 - tmp53)
			tmp55 = struct.unpack('I', tmp54)[0]
			
			self.ghosts = []
			for tmp56 in range(tmp55):
				tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp58:
					tmp57 = Ghost()
					offset = tmp57.deserialize(s, offset)
				else:
					tmp57 = None
				self.ghosts.append(tmp57)
		else:
			self.ghosts = None
		
		# deserialize self.constants
		tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp59:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
