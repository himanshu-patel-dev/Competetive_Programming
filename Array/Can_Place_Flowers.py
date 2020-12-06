'''
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent 
plots.

Given an integer array flowerbed containing 0's and 1's, where 0 
means empty and 1 means not empty, and an integer n, return if n 
new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule.

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        k = len(flowerbed)
        count = 0
        
        if n == 0:
            return True
        if k == 1:
            if n > 1: return False
            if flowerbed[0] == 0: return True
            return False
        
        count = 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[i] = 1
        
        if flowerbed[k-1] == 0 and flowerbed[k-2] == 0:
            count += 1
            flowerbed[k-1] = 1

        # for i in range(1,k-1):
        i = 1
        while i < k-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
                i += 2
            else:
                i += 1

            if count == n:
                return True

        return count >= n
