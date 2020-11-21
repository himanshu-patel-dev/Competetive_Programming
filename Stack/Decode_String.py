
'''
Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''

'''
Solution:
T = O()
'''
class Solution:
	def decodeString(self, s):
		stack = []

		for c in s:
			# put each char in stack if its not ']'
			if c != ']':
				stack.append(c)
				continue

			# if curr ele is end of a bracket then pop the 
			# string in bw two [ and ] in MiddleString
			MiddleString = []
			while stack and stack[-1] != '[':
				MiddleString.append(stack.pop())
			MiddleString = ''.join(MiddleString[::-1])

			stack.pop()	# pop out [

			# pop out the number associated with MiddleString
			num = []
			while stack and stack[-1].isdigit():
				num.append(stack.pop())
			num = ''.join(num[::-1])

			stack.extend( list(int(num)*MiddleString) )
		
		return ''.join(stack)


if __name__ == "__main__":
	s = Solution()

	print( s.decodeString('3[a]2[bc]') )
	print( s.decodeString('3[a2[c]]') )
	print( s.decodeString('2[abc]3[cd]ef') )
	print( s.decodeString('abc3[cd]xyz') )
