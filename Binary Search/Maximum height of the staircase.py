"""

Maximum height of the staircase
Problem Description
Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks. The first stair would require only one block, the second stair would require two blocks and so on. Find and return the maximum height of the staircase. 


Problem Constraints
0 <= A <= 10^9


Input Format
The only argument given is integer A.


Output Format
Return the maximum height of the staircase using these blocks.


Example Input
Input 1:
 A = 10
Input 2:
 20


Example Output
Output 1:
 4
Output 2:
 5


"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
    	
        # Math Approach
        # n = 1
        # count = 0
        # while(n*(n+1)//2 <= A):
        #     count += 1
        #     n += 1
        # return count
        


        # Binary Search Approach
        low = 0
        high = 10**9
        ans = float("-inf")
        while(low <= high):
            mid = low + (high-low)//2
            sum_upto_mid = mid*(mid+1)//2
            if sum_upto_mid == A:
                return mid
            elif sum_upto_mid < A:
                ans = max(ans, mid)
                low = mid+1
            else:
                high = mid-1
        return ans
