"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""

class Solution:
	""" 
	The goal is to make sure that the indices of each character 
	and word match up. As soon as we find a mismatch, we can return False. 
	"""
	def wordPattern(self, pattern: str, s: str) -> bool:
		word = s.split()
		dct = {}
		if len(pattern) != len(word):
			return False
		
		for i in range(len(pattern)):
			char_key = "char_" + pattern[i]
			word_key = "word_" + word[i]
			
			# recording only first occurance of each char and word
			# if a ele have two diff image or a image have two diff pre image 
			# then it update to latest image id or pre image id 
			if char_key not in dct:
				dct[char_key] = i
			if word_key not in dct:
				dct[word_key] = i
			
			# if we found any case where a lhs char is mapped to different word in rhs
			# or a rhs word is mapped to different word in lhs then this condition
			# condition become true
			if dct[word_key] != dct[char_key]:
				return False
		return True	