'''
Given an integer n, return any array containing n unique integers 
such that they add up to 0.
'''

class Solution:
    def sumZero(self, n):
        '''
            n = 1, [0]
            n = 2, [-1, 1]
            n = 3, [-2, 0, 2]
            n = 4, [-3, -1, 1, 3]
            n = 5, [-4, -2, 0, 2, 4]
        '''
        return range(1-n,n,2)

if __name__ == "__main__":
	s = Solution()

	n = 5
	print(list(s.sumZero(n)))

	n = 6
	print(list(s.sumZero(n)))
