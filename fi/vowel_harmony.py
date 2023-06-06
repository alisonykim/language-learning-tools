#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vowel_harmony.py

"""Master Finnish vowel harmony."""

from typing import List


def get_vowels(word: str) -> List[str]:
	vowels = 'aäeioöuy'
	return [char.lower() for char in word if char in vowels]


def return_vowel_group(word: str) -> str:
	"""
	Determine the vowel group that preserves vowel harmony for ```word```.
	
	Rules:
		1. All vowels of ```word``` in "AOU" or "AOUIE" -> "AOU"
		2. All vowels of ```word``` in "ÄÖY", "AÖYIE", or "IE" -> "ÄÖY"
	
	Note:
		Assumes that ```word``` is NOT a compound and has native Finnish etymology: a native non-compound word cannot contain vowels from the group {a, o, u} *together* with vowels from the group {ä, ö, y}.
	
	Example:
	>>> word1 = 'Oulu'
	>>> word2 = 'Jyväskylää'
	>>> word3 = 'Helsingi'
	>>> word4 = 'Rovaniemi'
	>>> return_vowel_group(word1)
	'aou'
	>>> return_vowel_group(word2)
	'äöy'
	>>> return_vowel_group(word3)
	'äöy'
	>>> return_vowel_group(word4)
	'aou'
	"""
	vowels = get_vowels(word)
	if any(vowel in 'äöy' for vowel in vowels) or all(vowel in 'ie' for vowel in vowels):
		return 'äöy'
	return 'aou'


def give_example_endings(word: str) -> str:
	"""Provide an example of an ending for ```word```, given its vowel harmony group."""
	if return_vowel_group(word) == 'aou':
		return '-ssa, -vat, -ko'
	return '-ssä, -vät, -kö'


if __name__ == '__main__':
	word = input('Enter a native Finnish, non-compound word: ')
	if not word:
		raise NameError(f'You must provide an input.')
	
	harmony_group = return_vowel_group(word)
	print(f'The corresponding vowel group for "{word}": {harmony_group}')
	valid_endings = give_example_endings(word)
	print(f'Examples of valid endings: {valid_endings}')