"""

Painter's Partition Problem
Problem Description
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of board.
 Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board. NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. Which means a configuration where painter 1 paints board 1 and 3 but not 2 is invalid.

Return the ans % 10000003.         


Problem Constraints
1 <= A <= 1000
1 <= B <= 10^6
1 <= N <= 10^5
1 <= C[i] <= 10^6


Input Format
The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer array C.


Output Format
Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board % 10000003.


Example Input
Input 1:
 A = 2
 B = 5
 C = [1, 10]
Input 2:
 A = 10
 B = 1
 C = [1, 8, 11, 3]
        


Example Output
Output 1:
 50
Output 2:
 11
        


Example Explanation
Explanation 1:
 Possibility 1:- One painter paints both blocks, time taken = 55 units.
 Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
 There are no other distinct ways to paint boards.
 ans = 50%10000003
Explanation 2:  
 Each block is painted by a painter so, Painter 1 paints block 1, painter 2 paints block 2, painter 3 paints block 3 
 and painter 4 paints block 4, time taken = max(1, 8, 11, 3) = 11
 ans = 11%10000003

"""

class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, painters, time, boards):
	    n = len(boards)
	    def isPossible(k,painters):
	        s = 0
	        count = 1
	        for board in boards:
	            s += board
	            if s>k:
	                count+=1
	                s = board
	        
	        return count<=painters
	    
	    low = max(boards)
	    high = sum(boards)
	    ans = 0
	    while(low<=high):
	        mid = low+(high-low)//2
	        if isPossible(mid,painters):
	            ans = mid % 10000003
	            high = mid-1
	        else:
	            low = mid+1
	    return (ans*time)% 10000003
	    
