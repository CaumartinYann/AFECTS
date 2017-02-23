#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The 'ProportionFloatValues' module.
"""


from Proportion import Proportion
from FloatValues import FloatValues


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class ProportionFloatValues(Proportion, FloatValues):

	def __init__(self, nameChar, level):

		super(ProportionFloatValues, self).__init__(nameChar, level)
