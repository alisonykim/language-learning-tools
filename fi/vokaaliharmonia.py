#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vokaaliharmonia.py

"""
Master Finnish vowel harmony.

Rules for native non-compound Finnish words:
	1. All vowels of ```word``` in "IE" -> neutral
	2. All vowels of ```word``` in "AOU" -> front
	3. All vowels of ```word``` in "AOUIE" -> front + neutral
	4. All vowels of ```word``` in "ÄÖY" -> back
	5. All vowels of ```word``` in "ÄÖYIE" -> back + neutral
"""

from termcolor import colored

import utils


def return_vowel_group(word: str) -> str:
	"""
	Determine the vowel group that preserves vowel harmony for ```word```.
	
	Note:
		Assumes that ```word``` is NOT a compound and has native Finnish etymology: a native non-compound word cannot contain vowels from the group {a, o, u} *together* with vowels from the group {ä, ö, y}.
	
	Example:
	>>> word1 = 'Suomi' # "UOI" in "AOUIE"
	>>> word2 = 'Sveitsi' # "EII" in "IE"
	>>> word3 = 'Saksa' # "AA" in "AOU"
	>>> word4 = 'Venäjä' # "EÄÄ" in "ÄÖYIE"
	>>> return_vowel_group(word1)
	'front + neutral'
	>>> return_vowel_group(word2)
	'neutral'
	>>> return_vowel_group(word3)
	'front'
	>>> return_vowel_group(word4)
	'back + neutral'
	"""
	vowels = [vowel[1] for vowel in utils.get_vowels_and_indices(word)]
	if not vowels:
		return f'inconclusive: "{word}" does not contain vowels'
	elif all(vowel in 'ie' for vowel in vowels): # Rule 1
		return 'neutral'
	elif all(vowel in 'aou' for vowel in vowels): # Rule 2
		return 'front'
	elif all(vowel in 'aouie' for vowel in vowels): # Rule 3
		return 'front + neutral'
	elif all(vowel in 'äöy' for vowel in vowels): # Rule 4
		return 'back'
	elif all(vowel in 'äöyie' for vowel in vowels): # Rule 5
		return 'back + neutral'
	else:
		return None


def give_example_endings(word: str) -> str:
	"""Provide example endings for ```word```, given its vowel harmony group."""
	vowel_group = return_vowel_group(word)
	if vowel_group in ['neutral', 'back', 'back + neutral']:
		return '-ssä, -vät, -kö'
	elif vowel_group in ['front', 'front + neutral']:
		return '-ssa, -vat, -ko'
	else:
		return 'unknown'


if __name__ == '__main__':
	print('-' * 89)
	word = input('Enter a native Finnish, non-compound word:\n')
	if not word:
		raise NameError(f'You must provide an input.')
	
	print('')
	vowel_group = return_vowel_group(word)
	print(f'The corresponding vowel group for \033[1m{colored(word.upper(), "blue")}\033[0m: {vowel_group}')
	valid_endings = give_example_endings(word)
	print(f'Examples of valid endings: {colored(valid_endings, "blue")}')
	print('-' * 89)