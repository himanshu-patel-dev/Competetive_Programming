"""
Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  
The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the 
robot never leaves the circle.

 

Example 1:
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to 
(0,0). When repeating these instructions, the robot remains in the circle 
of radius 2 centered at the origin.

Example 2:
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        # 0 is up, 1 is right, 2 is down, 3 is left
        direction = 0
        
        for move in instructions:
            if move == 'L':
                direction = (direction-1)%4
            elif move == 'R':
                direction = (direction+1)%4
            else:
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                else:
                    x -= 1 
        
        # robot do not move anywhere or return to origin back
        if x == 0 and y == 0:
            return True
        
        # if robot is facing diff than north direction at end then after 
        # some repetetion it will form a circle
        if direction != 0:
            return True
        else:
        # if robot is still facing north direction and had moved from 
        # its position then its not possible to form a circle, beaciuse 
        # in reoetetion robot will end up facing the same dir and move from its place
            return False
        
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        d=(0,1)
        for inst in instructions:
            if inst=='G':
                x,y=x+d[0],y+d[1]
            elif inst=='L':
                d=(-d[1],d[0])
            else:
                d=(d[1],-d[0])
        return (x==0 and y==0) or d!=(0,1)
        