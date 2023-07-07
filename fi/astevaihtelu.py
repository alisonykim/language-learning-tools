#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# astevaihtelu.py

"""
Master Finnish consonant gradation (FI: "astevaihtelu"), the phenomenon of certain consonants undergoing change when adding particular case endings to words.

WORDTYPE A GRADATION occurs when the nominative form (base) is STRONG. The last syllable becomes closed and transforms the following STRONG endings:
	S1. nominative singular
	S2. partitive
	S3. illative
	S4. essive
	S5. comitative
into one of the following WEAK endings:
	W1. nominative plural: "-t"
	W2. genitive: "-n"
	W3. inessive: "-ssa/ssä"
	W4. elative: "-sta/stä",
	W5. adessive: "-lla/llä"
	W6. ablative: "-lta/ltä"
	W7. allative: "-lle"
	W8. translative: "-ksi"
	W9. abessive: "-tta"
	W10. instructive: "-in"
"""

from termcolor import colored
from typing import Tuple, Union

import re

import constants
import utils


def get_transformation(word: str) -> Union[Tuple[str, str, str], None, str]:
	"""
	Perform consonant gradation from strong to weak forms.
	
	Returns:
		If ```word``` has a final syllable whose consonant(s) undergo grandation, then a tuple of the strong form, weak form, and transformed final syllable is returned. If ```word``` does not undergo consonant gradation, then an empty string is returned.
	
	Examples:
	>>> word1 = 'Afrikka'
	>>> get_transformation(word1)
	('kk', 'k', 'ka')
	>>> word2 = 'Hollanti'
	>>> get_transformation(word2)
	('nt', 'nn', 'nni')
	>>> word3 = 'Suomi'
	>>> get_transformation(word3)
	The word "Suomi" either does not undergo consonant gradation or the correct gradation is not currently recognized by this script.
	''
	"""
	final_syllable = utils.get_final_syllable(word)
	final_syllable_consonants = ''.join([consonant[1] for consonant in utils.get_consonants_and_indices(final_syllable)])
	try:
		if final_syllable_consonants[-2:] in constants.STRONG_TO_WEAK_GRAD.keys():
			target_consonants = final_syllable_consonants[-2:]
		elif final_syllable_consonants[-1] in constants.STRONG_TO_WEAK_GRAD.keys():
			target_consonants = final_syllable_consonants[-1]
		weak_form = constants.STRONG_TO_WEAK_GRAD[target_consonants]
		transformation = re.sub(target_consonants, weak_form, final_syllable, flags=re.IGNORECASE)
		return target_consonants, weak_form, transformation
	except KeyError:
		print(f'The word {colored(word.upper(), "blue")} either does not undergo consonant gradation or the correct gradation is not currently recognized by this script.')
		return ''


def produce_nom_plural_example(word: str) -> Union[str, None]:
	"""Give an example of a nominative plural transformation."""
	preceding_syllables = utils.get_preceding_syllables(word)
	try:	
		transformation = get_transformation(word)[2]
		return preceding_syllables + transformation + 't'
	except:
		return word + 't'


if __name__ == '__main__':
	print('-' * 89)
	word = input('Please input a Wordtype A nominal (nom. sing.):\n')
	print('')
	guess_strong = input('Which consonant(s) do you think undergo/es gradation?:\n')
	print('')
	guess_weak = input('Which consonant(s) do you think is/are produced from gradation?:\n')
	forms = get_transformation(word)
	example = produce_nom_plural_example(word)
	print('')

	if example == word + 't':
		if not guess_strong and not guess_weak:
			print('\033[1m')
			print('Correct!')
			print('\033[0m')
			print('')
			print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m does not undergo consonant gradation.')
			print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')
		else:
			print('\033[1m')
			print('Incorrect!')
			print('\033[0m')
			print('')
			print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m does not undergo consonant gradation.')
			# print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')
	else:
		if forms is not None and len(forms) == 3:
			strong, weak, transformation = forms
			if not guess_weak:
				weak = ''
			
			if strong == guess_strong and weak == guess_weak:
				print('\033[1m')
				print('Correct!')
				print('\033[0m')
				print('')
				if example == word + 't':
					print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m does not undergo consonant gradation.')
				else:
					print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m undergoes the following consonant gradation: {strong} -> \033[1m{colored(weak, "blue")}\033[0m')
					# print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')				
			elif strong == guess_strong and weak != guess_weak:
				print('\033[1m')
				print('Half correct!')
				print('\033[0m')
				print(f'You guessed the correct STRONG form \033[1m{guess_strong}\033[0m.')
				print(f'However, you guessed the wrong WEAK form: it is not {guess_weak}, but rather \033[1m{colored(weak, "blue")}\033[0m.')
				print('')
				print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m undergoes the following consonant gradation: {strong} -> \033[1m{colored(weak, "blue")}\033[0m.')
				# print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')
			elif strong != guess_strong and weak == guess_weak:
				print('\033[1m')
				print('Half correct!')
				print('\033[0m')
				print('')
				print(f'You guessed the correct WEAK form {guess_weak}.')
				print(f'However, you guessed the wrong STRONG form: it is not {guess_strong}, but rather \033[1m{strong}\033[0m.')
				print('')
				print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m undergoes the following consonant gradation: {strong} -> \033[1m{colored(weak, "blue")}\033[0m.')
				# print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')
			else:
				print(f'Incorrect!')
				print('')
				print(f'You guessed the STRONG form {guess_strong} and WEAK form {guess_weak}.')
				print('')
				print(f'The word {colored(word.upper(), "blue")} undergoes the following consonant gradation: {strong} -> \033[1m{colored(weak, "blue")}\033[0m.')
				# print(f'The nominative plural form of {colored(word.upper(), "blue")} is {example}.')
		else:
			print(f'The word \033[1m{colored(word.upper(), "blue")}\033[0m either does not undergo consonant gradation or its gradation is not recognized by the script at this time.')
	
	print('-' * 89)