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
	try:
		for strong_form in constants.STRONG_TO_WEAK_GRAD.keys():
			if strong_form in final_syllable:
				weak_form = constants.STRONG_TO_WEAK_GRAD[strong_form]
				transformation = re.sub(strong_form, weak_form, final_syllable, flags=re.IGNORECASE)
				return strong_form, weak_form, transformation
	except KeyError:
		print(f'The word "{word}" either does not undergo consonant gradation or the correct gradation is not currently recognized by this script.')
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
	word = input('Please input a Wordtype A word: ')
	guess_strong = input('Which consonant(s) do you think undergo gradation?: ')
	guess_weak = input('Which consonant(s) do you think are produced from gradation?: ')
	forms = get_transformation(word)
	example = produce_nom_plural_example(word)

	print('')

	if example == word + 't':
		if not guess_strong and not guess_weak:
			print('Correct!')
			print('')
			print(f'The word "{word}" does not undergo consonant gradation.')
			print(f'The nominative plural form of "{word}" is "{example}".')
		else:
			print('Incorrect!')
			print('')
			print(f'The word "{word}" does not undergo consonant gradation.')
			print(f'The nominative plural form of "{word}" is "{example}".')
	else:
		if forms is not None and len(forms) == 3:
			strong, weak, transformation = forms
			if not guess_weak:
				weak = ''
			
			if strong == guess_strong and weak == guess_weak:
				print('Correct!')
				print('')
				if example == word + 't':
					print(f'The word "{word}" does not undergo consonant gradation.')
				else:
					print(f'The word "{word}" undergoes the following consonant gradation: "{strong}" -> "{weak}"')
					print(f'The nominative plural form of "{word}" is "{example}".')				
			elif strong == guess_strong and weak != guess_weak:
				print(f'Half correct!')
				print('')
				print(f'You guessed the correct STRONG form "{guess_strong}".')
				print(f'However, you guessed the wrong WEAK form: it is not "{guess_weak}", but rather "{weak}".')
				print('')
				print(f'The word "{word}" undergoes the following consonant gradation: "{strong}" -> "{weak}".')
				print(f'The nominative plural form of "{word}" is "{example}".')
			elif strong != guess_strong and weak == guess_weak:
				print(f'Half correct!')
				print('')
				print(f'You guessed the correct WEAK form "{guess_weak}".')
				print(f'However, you guessed the wrong STRONG form: it is not "{guess_strong}", but rather "{strong}".')
				print('')
				print(f'The word "{word}" undergoes the following consonant gradation: "{strong}" -> "{weak}".')
				print(f'The nominative plural form of "{word}" is "{example}".')
			else:
				print(f'Incorrect!')
				print('')
				print(f'You guessed the STRONG form "{guess_strong}" and WEAK form "{guess_weak}".')
				print('')
				print(f'The word "{word}" undergoes the following consonant gradation: "{strong}" -> "{weak}".')
				print(f'The nominative plural form of "{word}" is "{example}".')
		else:
			print(f'The word "{word}" either does not undergo consonant gradation or its gradation is not recognized by the script at this time.')