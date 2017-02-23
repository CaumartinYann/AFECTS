#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
An custom exception if we use an attribute of a class BEFORE having solved the system.
"""


import Exception


__author__ = "HorlogeSkynet"
__copyright__ = "Copyright 2017, AFECTS"
__license__ = "GPLv3"


class InstanceNotSet(Exception):

	def __init__(self, arg):

		super(InstanceNotSet, self).__init__()

		self.arg = arg

	def __str__(self):

		print('This system has not been solved, you can\'t use this attribute yet.')
