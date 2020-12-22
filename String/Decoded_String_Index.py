'''
An encoded string S is given.  To find and write the decoded string to a tape, 
the encoded string is read one character at a time and the following steps are 
taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly 
written d-1 more times in total. Now for some encoded string S, and an index K, 
find and return the K-th letter (1 indexed) in the decoded string.

Constraints:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
'''

class Solution:
	def decodeAtIndex(self, S, K):
		length = 0
		
		# get the lenght of decoded string in 'length'
		for c in S:
			if c.isalpha():
				length += 1
			else:
				length = length*int(c)
				
		# for each char in S keep dec the lenght by one 
		# for each char and divide len by int for each int
		# thus when K == remaining_length or K == 0 after modulo 
		# with K% remaining_length then return the current char 
		# or if current char is digit return next coming char
		for c in reversed(S):
			K = K % length
			
			if K == 0 and c.isalpha():
				return c
			
			if c.isalpha():
				length -= 1
			else:
				length = length//int(c)

if __name__ == "__main__":
	s = Solution()

	print(s.decodeAtIndex('leet2code3',10))
	print(s.decodeAtIndex('ha22',5))
	print(s.decodeAtIndex('a2345678999999999999999',1))
