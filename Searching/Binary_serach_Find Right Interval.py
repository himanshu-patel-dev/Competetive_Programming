"""
Given a set of intervals, for each of the interval i, check if there exists an 
interval j whose start point is bigger than or equal to the end point of the interval 
i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means 
that the interval j has the minimum start point to build the "right" relationship for 
interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, 
you need output the stored value of each interval as an array.

Input: [ [1,2] ]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.


Input: [ [3,4], [2,3], [1,2] ]
Output: [-1, 0, 1]
Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Input: [ [1,4], [2,3], [3,4] ]
Output: [-1, 2, -1]
Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

"""

def findRightInterval(intervals):
    import bisect
    
    n = len(intervals)
    # making a array which holds the first ele of each interval along with its index
    start_pos = [ (ele[0],i) for i,ele in enumerate(intervals)] + [ (float('inf'),-1) ]
    # sorting so that we can apply binary search on array to get number
    # of interval to right of any interval 
    start_pos.sort()
    
    # print(start_pos)
    result = []
    for i in range(n):
        # pass second index as a tuple because it will be compared with other tuples
        index = bisect.bisect_left(start_pos, (intervals[i][1],0) )
        # print(index,(intervals[i][1]))
        # store the index of interval having right relation
        # if no such index then -1 get stored
        result.append( start_pos[index][1] )
        
    # return result
    print(result)
    
if __name__ == "__main__":
    interval = [ [1,4], [2,3], [3,4] ]
    findRightInterval(interval)

    interval = [ [3,4], [2,3], [1,2] ]
    findRightInterval(interval)

    interval = [ [1,2] ]
    findRightInterval(interval)
