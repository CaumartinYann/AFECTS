#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'CharacteristicConstraint' module.
"""


from Constraint import Constraint


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class CharacteristicConstraint(Constraint):

	def __init__(self, nameChar, level):

		super(CharacteristicConstraint, self).__init__(nameChar, level)
