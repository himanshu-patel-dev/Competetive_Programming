"""
Given a string s, remove duplicate letters so that every letter appears 
once and only once. You must make sure your result is the smallest in 
lexicographical order among all possible results.
"""
class Solution:
	def removeDuplicateLetters(self, s):
		last_occ = {c:i for i,c in enumerate(s)}
		stack = []
		visited = set()

		for i,c in enumerate(s):
			# if ele is alredy prcessed no need to add its duplicates
			if c in visited:
				continue

			# while the ele at top of stack is grater then current element
			# and is also present after current ele in string (larger last occutance)
			# pop them from stack and remove them from visited
			while stack and stack[-1] > c and last_occ[stack[-1]] > i:
				visited.remove( stack.pop() )

			stack.append(c)
			visited.add(c)

		return ''.join(stack)


if __name__ == "__main__":
	s = Solution()

	string = "bcabc"
	print( s.removeDuplicateLetters(string) )

	string = "cbacdcbc"
	print( s.removeDuplicateLetters(string) )