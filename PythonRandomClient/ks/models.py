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


	def __init__(self, food_score=None, super_food_score=None, ghost_death_score=None, pacman_death_score=None, pacman_max_health=None, pacman_giant_form_duration=None, max_cycles=None):
		self.initialize(food_score, super_food_score, ghost_death_score, pacman_death_score, pacman_max_health, pacman_giant_form_duration, max_cycles)
	

	def initialize(self, food_score=None, super_food_score=None, ghost_death_score=None, pacman_death_score=None, pacman_max_health=None, pacman_giant_form_duration=None, max_cycles=None):
		self.food_score = food_score
		self.super_food_score = super_food_score
		self.ghost_death_score = ghost_death_score
		self.pacman_death_score = pacman_death_score
		self.pacman_max_health = pacman_max_health
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
		
		# serialize self.pacman_max_health
		s += b'\x00' if self.pacman_max_health is None else b'\x01'
		if self.pacman_max_health is not None:
			s += struct.pack('i', self.pacman_max_health)
		
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
		
		# deserialize self.pacman_max_health
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.pacman_max_health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.pacman_max_health = None
		
		# deserialize self.pacman_giant_form_duration
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.pacman_giant_form_duration = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.pacman_giant_form_duration = None
		
		# deserialize self.max_cycles
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.max_cycles = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_cycles = None
		
		return offset


class Pacman(object):

	@staticmethod
	def name():
		return 'Pacman'


	def __init__(self, x=None, y=None, direction=None, health=None, giant_form_remaining_time=None):
		self.initialize(x, y, direction, health, giant_form_remaining_time)
	

	def initialize(self, x=None, y=None, direction=None, health=None, giant_form_remaining_time=None):
		self.x = x
		self.y = y
		self.direction = direction
		self.health = health
		self.giant_form_remaining_time = giant_form_remaining_time
	

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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.direction
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			tmp10 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp10)
		else:
			self.direction = None
		
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


class Ghost(object):

	@staticmethod
	def name():
		return 'Ghost'


	def __init__(self, id=None, x=None, y=None, direction=None):
		self.initialize(id, x, y, direction)
	

	def initialize(self, id=None, x=None, y=None, direction=None):
		self.id = id
		self.x = x
		self.y = y
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.x
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.direction
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			tmp17 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp17)
		else:
			self.direction = None
		
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
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.board))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			for tmp19 in self.board:
				s += b'\x00' if tmp19 is None else b'\x01'
				if tmp19 is not None:
					tmp20 = b''
					tmp20 += struct.pack('I', len(tmp19))
					while len(tmp20) and tmp20[-1] == b'\x00'[0]:
						tmp20 = tmp20[:-1]
					s += struct.pack('B', len(tmp20))
					s += tmp20
					
					for tmp21 in tmp19:
						s += b'\x00' if tmp21 is None else b'\x01'
						if tmp21 is not None:
							s += struct.pack('b', tmp21.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp22 = b''
			tmp22 += struct.pack('I', len(self.scores))
			while len(tmp22) and tmp22[-1] == b'\x00'[0]:
				tmp22 = tmp22[:-1]
			s += struct.pack('B', len(tmp22))
			s += tmp22
			
			for tmp23 in self.scores:
				s += b'\x00' if tmp23 is None else b'\x01'
				if tmp23 is not None:
					tmp24 = b''
					tmp24 += struct.pack('I', len(tmp23))
					while len(tmp24) and tmp24[-1] == b'\x00'[0]:
						tmp24 = tmp24[:-1]
					s += struct.pack('B', len(tmp24))
					s += tmp24
					
					s += tmp23.encode('ISO-8859-1') if PY3 else tmp23
				s += b'\x00' if self.scores[tmp23] is None else b'\x01'
				if self.scores[tmp23] is not None:
					s += struct.pack('i', self.scores[tmp23])
		
		# serialize self.pacman
		s += b'\x00' if self.pacman is None else b'\x01'
		if self.pacman is not None:
			s += self.pacman.serialize()
		
		# serialize self.ghosts
		s += b'\x00' if self.ghosts is None else b'\x01'
		if self.ghosts is not None:
			tmp25 = b''
			tmp25 += struct.pack('I', len(self.ghosts))
			while len(tmp25) and tmp25[-1] == b'\x00'[0]:
				tmp25 = tmp25[:-1]
			s += struct.pack('B', len(tmp25))
			s += tmp25
			
			for tmp26 in self.ghosts:
				s += b'\x00' if tmp26 is None else b'\x01'
				if tmp26 is not None:
					s += tmp26.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp31 = s[offset:offset + tmp30]
			offset += tmp30
			tmp31 += b'\x00' * (4 - tmp30)
			tmp32 = struct.unpack('I', tmp31)[0]
			
			self.board = []
			for tmp33 in range(tmp32):
				tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp35:
					tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp37 = s[offset:offset + tmp36]
					offset += tmp36
					tmp37 += b'\x00' * (4 - tmp36)
					tmp38 = struct.unpack('I', tmp37)[0]
					
					tmp34 = []
					for tmp39 in range(tmp38):
						tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp41:
							tmp42 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp40 = ECell(tmp42)
						else:
							tmp40 = None
						tmp34.append(tmp40)
				else:
					tmp34 = None
				self.board.append(tmp34)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp45 = s[offset:offset + tmp44]
			offset += tmp44
			tmp45 += b'\x00' * (4 - tmp44)
			tmp46 = struct.unpack('I', tmp45)[0]
			
			self.scores = {}
			for tmp47 in range(tmp46):
				tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp50:
					tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp52 = s[offset:offset + tmp51]
					offset += tmp51
					tmp52 += b'\x00' * (4 - tmp51)
					tmp53 = struct.unpack('I', tmp52)[0]
					
					tmp48 = s[offset:offset + tmp53].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp53]
					offset += tmp53
				else:
					tmp48 = None
				tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp54:
					tmp49 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp49 = None
				self.scores[tmp48] = tmp49
		else:
			self.scores = None
		
		# deserialize self.pacman
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			self.pacman = Pacman()
			offset = self.pacman.deserialize(s, offset)
		else:
			self.pacman = None
		
		# deserialize self.ghosts
		tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp56:
			tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp58 = s[offset:offset + tmp57]
			offset += tmp57
			tmp58 += b'\x00' * (4 - tmp57)
			tmp59 = struct.unpack('I', tmp58)[0]
			
			self.ghosts = []
			for tmp60 in range(tmp59):
				tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp62:
					tmp61 = Ghost()
					offset = tmp61.deserialize(s, offset)
				else:
					tmp61 = None
				self.ghosts.append(tmp61)
		else:
			self.ghosts = None
		
		# deserialize self.constants
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
