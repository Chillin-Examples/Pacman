# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECommandDirection(Enum):
	Up = 0
	Right = 1
	Down = 2
	Left = 3


class ChangePacmanDirection(object):

	@staticmethod
	def name():
		return 'ChangePacmanDirection'


	def __init__(self, direction=None):
		self.initialize(direction)
	

	def initialize(self, direction=None):
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.direction
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			tmp1 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = ECommandDirection(tmp1)
		else:
			self.direction = None
		
		return offset


class ChangeGhostDirection(object):

	@staticmethod
	def name():
		return 'ChangeGhostDirection'


	def __init__(self, id=None, direction=None):
		self.initialize(id, direction)
	

	def initialize(self, id=None, direction=None):
		self.id = id
		self.direction = direction
	

	def serialize(self):
		s = b''
		
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
		# deserialize self.id
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			tmp4 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = ECommandDirection(tmp4)
		else:
			self.direction = None
		
		return offset
