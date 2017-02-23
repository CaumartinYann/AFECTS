#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'FloatValues' module.
"""


from CharacteristicConstraint import CharacteristicConstraint


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class FloatValues(CharacteristicConstraint):

	def __init__(self, nameChar, level, type_):

		super(FloatValues, self).__init__(nameChar, level)

		self.type_ = type_

	def getType(self):

			return self.type_

	def setType(self, type_):

		self.type_ = type_
