"""
In a country popular for train travel, you have planned some train travelling 
one year in advance. The days of the year that you will travel is given as an 
array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get 
a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the 'minimum number' of dollars you need to travel every day in the given list of days.


Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # make a dp array with 1 more than the days given
        n = days[-1] + 1
        dp = [0]*n
        days = set(days)
        
        
        for day in range(1,n):
            if day in days:
                # get the cost on previous days
                one_day = dp[day-1] + costs[0]
                seven_day = dp[ max(0,day-7) ] + costs[1]
                thirty_day = dp[ max(0,day-30) ] + costs[2]
                # choose the min one
                dp[day] = min(one_day, seven_day, thirty_day)
                
            else:
                # we dont have to travel on this day
                dp[day] = dp[day-1]
        # print(dp)
        return dp[-1]
