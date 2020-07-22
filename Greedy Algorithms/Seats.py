"""

Seats
Problem Description

There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

In one jump a person can move to the adjacent seat (if available).

NOTE: 1. Return your answer modulo 10^7 + 3.



Problem Constraints
1 <= N <= 1000000
A[i] = 'x' or '.'



Input Format
First and only argument is a string A of size N.



Output Format
Return an integer denoting the minimum number of jumps required.



Example Input
Input 1:

 A = "....x..xx...x.."
Input 2:

 A = "....xxx"


Example Output
Output 1:

 5
Output 2:

 0


Example Explanation
Explanation 1:

 Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) 
                 . . . . x . . x x . . . x . . 
 Now to make them sit together one of approaches is -
                 . . . . . . x x x x . . . . .
 Steps To achieve this:
 1) Move the person sitting at 4th index to 6th index: Number of jumps by him =   (6 - 4) = 2
 2) Bring the person sitting at 12th index to 9th index: Number of jumps by him = (12 - 9) = 3
 So, total number of jumps made: 2 + 3 = 5 which is the minimum possible.

 If we other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.
 
Explanation 2:

 They are already together. So, the cost is zero.

"""


import math

def countPersons(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 'x':
            count += 1
    return count
    
    
def findMiddlePersonIndex(A, count):
    mid = math.ceil(count/2)
	temp = 0
	index = -1
	for i in range(len(A)):
	    if A[i] == 'x':
	        temp += 1
	    if temp == mid:
	        index = i
	        break
	return index
    

# For finding closest vacant seat in left direction of middle person    
def findLeftVacantSeat(A, index):
    left = -1
    i = index-1
	while i >= 0:
	    if A[i] == '.':
	        left = i
	        break
	    i -= 1
    return left
    

# For finding closest vacant seat in right direction of middle person  
def findRightVacantSeat(A, index):
    n = len(A)
    right = n
	j = index+1
	while j < n:
	    if A[j] == '.':
	        right = j
	        break
	    j += 1
	return right


class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
	    n = len(A)
	    jumps = 0
	    
	    count = countPersons(A)
	    index = findMiddlePersonIndex(A, count)        
	    left = findLeftVacantSeat(A, index)
	    right = findRightVacantSeat(A, index)
	        
	    # For the persons in left direction from the middle
	    for i in range(left-1, -1, -1):
	        if A[i] == 'x':
	            jumps = (jumps + left - i)%(10**7+3)
	            left -= 1
	            
	    # For the persons in right direction from the middle         
	    for i in range(right+1, n):
	        if A[i] == 'x':
	            jumps = (jumps + i - right)%(10**7+3)
	            right += 1
	            
	    return jumps
	    
	    
	    
