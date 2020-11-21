'''
There are 1000 buckets, one and only one of them is poisonous, while the rest are 
filled with water. They all look identical. 
If a pig drinks the poison it will die within 15 minutes. 
What is the minimum amount of pigs you need to figure out which bucket is poisonous 
within one hour?

Answer this question, and write an algorithm for the general case.

General case:
If there are n buckets and a pig drinking poison will die within m minutes, 
how many pigs (x) you need to figure out the poisonous bucket within p minutes? 
There is exactly one bucket with poison.

Note:

A pig can be allowed to drink simultaneously on as many buckets as one would like, 
and the feeding takes no time.
After a pig has instantly finished drinking buckets, there has to be a cool down 
time of m minutes. During this time, only observation is allowed and no feedings 
at all.
Any given bucket can be sampled an infinite number of times (by an unlimited 
number of pigs).
'''

'''
Solution:

let k = minutesToTest // minutesToDie is total no of complete test we can make 
before timeout but in actual we can make k+1 verification. as the last optioin need 
no test

# 1. if the no of pigs is equal or less then T = k+1

buckets = 1,2,3,4,5 then with 60 min total and 15 min to die we can make 60//15 test
but 4+1 = 5 verification as we with 4 test we can test 4 buckets and 5th we dont 
need to test as we are sure it has poison (exactly one bucker poisonous)

# if no of pigs is more than T = k+1 and less then T^2 then we need 2 pigs

if there are 25 pigs we can identify row and col of intersect

1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

for each test one pig test complete row and anther test complete col for each test
interval thus within 5 verification we test out all 5 row and 5 col and intersection
give poison bucket

# if no of pig are more than T^2 and less than equal to T^3 then we need 3 pigs

consider a 3D cube with each face as 
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

here each of the three pig will test one surface the intersection of three surface 
will give poison bucket

thus if we can make T validation test then no of pig reuired are x then 
	T^x <= N

	or x = log(N) where log is T base and if x is fraction then take its ceil

'''

class Solution:
	''' slow '''
	def poorPigs(self, buckets, minutesToDie, minutesToTest):
		import math
		T = minutesToTest//minutesToDie + 1
		
		res = math.log(buckets)/math.log(T)
		return math.ceil( res )

class Solution:
	''' fast '''
	def poorPigs(self, buckets, minutesToDie, minutesToTest):
		import math
		pig = 0

		if minutesToDie == minutesToTest:
			return 2

		T = minutesToTest//minutesToDie + 1
		while (T)**pig < buckets:
			pig += 1
		return pig	
	

if __name__ == "__main__":
	s = Solution()
	
	buckets = 1000
	minutesToDie = 15
	minutesToTest = 60
	print( s.poorPigs(buckets, minutesToDie, minutesToTest) )

	buckets = 4
	minutesToDie = 15
	minutesToTest = 15
	print( s.poorPigs(buckets, minutesToDie, minutesToTest) )
