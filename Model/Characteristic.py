#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Characteristic' module.
There are two attributes, a value and its type. Its type is not the "variable type" of the value.
It indicates if the 'value' attribute represents a numerical or text value, OR a category...
"""


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Characteristic():

	def __init__(self, value, type_):

		self.value = value

		if type_ and (type_ == 'VALUE' or type_ == 'CATEGORY'):

			self.type_ = type_

		else:

			raise ValueError

	def getValue(self):

		return self.value

	def setValue(self, value):

		self.value = value

	def getType(self):

		return self.type_

	def setType(self, type_):

		if type_ and (type_ == 'VALUE' or type_ == 'CATEGORY'):

			self.type_ = type_

		else:

			raise ValueError
