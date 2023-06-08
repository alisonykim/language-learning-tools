#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# constants.py


FINNISH_VOWELS = 'aäeioöuy'

WORDTYPE_A_VOWELS = 'aäioöuy' # "e" does not belong to Wordtype A

STRONG_TO_WEAK_GRAD = {
	'kk': 'k',
	'pp': 'p',
	'tt': 't',
	'nk': 'ng',
	'nt': 'nn',
	'mp': 'mm',
	'lt': 'll',
	'rt': 'rr',
	'k': '',
	'p': 'v',
	't': 'd',
}