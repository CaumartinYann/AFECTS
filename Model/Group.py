#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Group' module.
You won't be able to initialize a group with a minimum [wanted] number of elements which is strictly below 1.
If you try to get the number of elements in the group while it's not "solved" yet, you'd get a exception raised (because only a range would be available at this time).
"""


from Element import Element
from InstanceNotSet import InstanceNotSet


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Group():

	def __init__(self, name, value, gap, constraints):

		self.name = name
		self.nbElements = (value + gap, value - gap if value > value else 1)
		self.characteristics = constraints

		self.elements = []

	def getName(self):

		return self.name

	def setName(self, name):

		self.name = name

	def getNbElements(self):

		if not isinstance(self.nbElements, int):

			raise InstanceNotSet

		else:

			return self.nbElements

	def setNbElements(self, nbElements):

		self.nbElements = nbElements

	def getConstraints(self):

		return self.constraints

	def addElement(self, element):

		if not isinstance(element, Element):

			raise TypeError

		else:

			self.elements.append(element)

	def removeElement(self, element):

		self.elements.remove(element)
