#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# utils.py

"""Utility functions for subword extractions, etc."""

from typing import List, Tuple

import constants


def get_consonants_and_indices(word: str) -> List[Tuple[int, str]]:
	"""Identify all consonants in ```word``` and their respective indices."""
	return [(idx, char) for idx, char in enumerate(word) if char not in constants.FINNISH_VOWELS]


def get_vowels_and_indices(word: str) -> List[Tuple[int, str]]:
	"""Identify all vowels in ```word``` and their respective indices."""
	return [(idx, char) for idx, char in enumerate(word) if char in constants.FINNISH_VOWELS]


def get_final_syllable(word: str) -> str:
	"""Extract the final syllable of ```word```."""
	if word[-1] not in constants.WORDTYPE_A_VOWELS:
		raise ValueError(f'The inputted word "{word}" does not belong to Wordtype A, where vowels must belong to: {constants.WORDTYPE_A_VOWELS}. Please try again with a Wordtype A word.')
	vowel_map = get_vowels_and_indices(word)
	try:
		idx, _ = vowel_map[-2]
		return ''.join([char for char in word[idx+1:]])
	except IndexError:
		if vowel_map[-1][1] != word[-1]:
			raise ValueError(f'The inputted word "{word}" does not belong to Wordtype A, which ends in one of the following vowels: {constants.WORDTYPE_A_VOWELS}. Please try again with a Wordtype A word.')
		raise ValueError(f'The inputted word "{word}" must have 2 or more syllables. Please try again with a multisyllabic word.')


def get_preceding_syllables(word: str) -> str:
	try:
		penultimate_vowel_idx = get_vowels_and_indices(word)[-2][0]
		return word[:penultimate_vowel_idx+1]
	except KeyError:
		raise ValueError(f'The inputted word "{word}" must have 2 or more syllables. Please try again with a multisyllabic word.')