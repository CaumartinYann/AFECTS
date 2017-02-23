#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Constraint' module.
A constraint has a name in order to identify itself, a level which represents its relevance.
Its level may take the values: 'HIGH', 'MEDIUM' and 'LOW'.
Once this constraint is solved in the system, the boolean 'solved' has to be manually set to 'True'.
"""


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Constraint():

	def __init__(self, nameChar, level):

		self.nameChar = nameChar

		if level and (level == 'HIGH' or level == 'MEDIUM' or level == 'LOW'):

			self.level = level

		else:

			raise ValueError

		self.solved = False

	def getNameChar(self):

		return self.nameChar

	def setNameChar(self, nameChar):

		self.nameChar = nameChar

	def getLevel(self):

		return self.level

	def setLevel(self, level):

		if level and (level == 'HIGH' or level == 'MEDIUM' or level == 'LOW'):

			self.level = level

		else:

			raise ValueError

	def isSolved(self):

		return self.solved
