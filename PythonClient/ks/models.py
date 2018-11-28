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
		
		return offset


class Ghost(object):

	@staticmethod
	def name():
		return 'Ghost'


	def __init__(self, x=None, y=None, id=None, direction=None):
		self.initialize(x, y, id, direction)
	

	def initialize(self, x=None, y=None, id=None, direction=None):
		self.x = x
		self.y = y
		self.id = id
		self.direction = direction
	

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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		# deserialize self.id
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			tmp16 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDirection(tmp16)
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
			tmp17 = b''
			tmp17 += struct.pack('I', len(self.board))
			while len(tmp17) and tmp17[-1] == b'\x00'[0]:
				tmp17 = tmp17[:-1]
			s += struct.pack('B', len(tmp17))
			s += tmp17
			
			for tmp18 in self.board:
				s += b'\x00' if tmp18 is None else b'\x01'
				if tmp18 is not None:
					tmp19 = b''
					tmp19 += struct.pack('I', len(tmp18))
					while len(tmp19) and tmp19[-1] == b'\x00'[0]:
						tmp19 = tmp19[:-1]
					s += struct.pack('B', len(tmp19))
					s += tmp19
					
					for tmp20 in tmp18:
						s += b'\x00' if tmp20 is None else b'\x01'
						if tmp20 is not None:
							s += struct.pack('b', tmp20.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp21 = b''
			tmp21 += struct.pack('I', len(self.scores))
			while len(tmp21) and tmp21[-1] == b'\x00'[0]:
				tmp21 = tmp21[:-1]
			s += struct.pack('B', len(tmp21))
			s += tmp21
			
			for tmp22 in self.scores:
				s += b'\x00' if tmp22 is None else b'\x01'
				if tmp22 is not None:
					tmp23 = b''
					tmp23 += struct.pack('I', len(tmp22))
					while len(tmp23) and tmp23[-1] == b'\x00'[0]:
						tmp23 = tmp23[:-1]
					s += struct.pack('B', len(tmp23))
					s += tmp23
					
					s += tmp22.encode('ISO-8859-1') if PY3 else tmp22
				s += b'\x00' if self.scores[tmp22] is None else b'\x01'
				if self.scores[tmp22] is not None:
					s += struct.pack('i', self.scores[tmp22])
		
		# serialize self.pacman
		s += b'\x00' if self.pacman is None else b'\x01'
		if self.pacman is not None:
			s += self.pacman.serialize()
		
		# serialize self.ghosts
		s += b'\x00' if self.ghosts is None else b'\x01'
		if self.ghosts is not None:
			tmp24 = b''
			tmp24 += struct.pack('I', len(self.ghosts))
			while len(tmp24) and tmp24[-1] == b'\x00'[0]:
				tmp24 = tmp24[:-1]
			s += struct.pack('B', len(tmp24))
			s += tmp24
			
			for tmp25 in self.ghosts:
				s += b'\x00' if tmp25 is None else b'\x01'
				if tmp25 is not None:
					s += tmp25.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp30 = s[offset:offset + tmp29]
			offset += tmp29
			tmp30 += b'\x00' * (4 - tmp29)
			tmp31 = struct.unpack('I', tmp30)[0]
			
			self.board = []
			for tmp32 in range(tmp31):
				tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp34:
					tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp36 = s[offset:offset + tmp35]
					offset += tmp35
					tmp36 += b'\x00' * (4 - tmp35)
					tmp37 = struct.unpack('I', tmp36)[0]
					
					tmp33 = []
					for tmp38 in range(tmp37):
						tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp40:
							tmp41 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp39 = ECell(tmp41)
						else:
							tmp39 = None
						tmp33.append(tmp39)
				else:
					tmp33 = None
				self.board.append(tmp33)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp42:
			tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp44 = s[offset:offset + tmp43]
			offset += tmp43
			tmp44 += b'\x00' * (4 - tmp43)
			tmp45 = struct.unpack('I', tmp44)[0]
			
			self.scores = {}
			for tmp46 in range(tmp45):
				tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp49:
					tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp51 = s[offset:offset + tmp50]
					offset += tmp50
					tmp51 += b'\x00' * (4 - tmp50)
					tmp52 = struct.unpack('I', tmp51)[0]
					
					tmp47 = s[offset:offset + tmp52].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp52]
					offset += tmp52
				else:
					tmp47 = None
				tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp53:
					tmp48 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp48 = None
				self.scores[tmp47] = tmp48
		else:
			self.scores = None
		
		# deserialize self.pacman
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.pacman = Pacman()
			offset = self.pacman.deserialize(s, offset)
		else:
			self.pacman = None
		
		# deserialize self.ghosts
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp57 = s[offset:offset + tmp56]
			offset += tmp56
			tmp57 += b'\x00' * (4 - tmp56)
			tmp58 = struct.unpack('I', tmp57)[0]
			
			self.ghosts = []
			for tmp59 in range(tmp58):
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp60 = Ghost()
					offset = tmp60.deserialize(s, offset)
				else:
					tmp60 = None
				self.ghosts.append(tmp60)
		else:
			self.ghosts = None
		
		# deserialize self.constants
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
