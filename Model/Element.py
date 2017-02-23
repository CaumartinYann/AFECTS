#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Element' module.
An element is able to make a wish to "be in the same group" with others elements.
It is also defined by its intrinsic characteristics.
"""

__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Element():

	def __init__(self, name, characteristics, wishes):

		self.name = name

		self.characteristics = characteristics
		self.wishes = wishes

	def getName(self):

		return self.name

	def setName(self, name):

		self.name = name

	def getCharacteristics(self):

		return self.characteristics

	def getWishes(self):

		return self.wishes
