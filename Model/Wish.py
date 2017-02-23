#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'Wish' module.
A wish is a particular constraint. It contains a list of 'Element' another 'Element' wants to be with.
It also got an attribute 'type_' in order to announce the type of constraint (the element wants to be with ALL of its wishes, or is it just a wishes order ?).
"""


from Constraint import Constraint


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class Wish(Constraint):

	def __init__(self, nameChar, level, type_, element):

		super(Wish, self).__init__(nameChar, level)

		if type_ and (type_ == 'ORDER' or type_ == 'ALL'):

			self.type_ = type_

		else:

			raise ValueError

		self.element = element

	def getType(self):

		return self.type_

	def setType(self, type_):

		if type_ and (type_ == 'ORDER' or type_ == 'ALL'):

			self.type_ = type_

		else:

			raise ValueError
