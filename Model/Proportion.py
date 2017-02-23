#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Proportion' module.
While the system is not solved, the 'percentage' attribute will be a tuple representing a range of wanted values.
Once the system is solved, it'll become the computed float value.
"""


from InstanceNotSet import InstanceNotSet
from CharacteristicConstraint import CharacteristicConstraint


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Proportion(CharacteristicConstraint):

	def __init__(self, nameChar, level, value, gap):

		super(Proportion, self).__init__(nameChar, level)

		self.percentage = (value + gap, value - gap if value >= gap else 0)

	def getPercentage(self):

		if not isinstance(self.percentage, float):

			raise InstanceNotSet

		else:

			return self.percentage

	def setPercentage(self, percentage):

		self.percentage = percentage
