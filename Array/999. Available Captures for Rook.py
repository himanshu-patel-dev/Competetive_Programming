# https://leetcode.com/problems/available-captures-for-rook/
from typing import *

class Solution:
	def numRookCaptures(self, board: List[List[str]]) -> int:
		rookX, rookY = next(((x,y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 'R'))
		count = 0
		dirs = [(1,0), (-1,0), (0,1), (0,-1)]
		for dx, dy in dirs:
			currX, currY = rookX, rookY
			while 0<=currX<len(board) and 0<=currY<len(board[0]):
				if board[currX][currY] == "B":
					break
				if board[currX][currY] == "p":
					count += 1
					break
			
				currX += dx
				currY += dy
		return count