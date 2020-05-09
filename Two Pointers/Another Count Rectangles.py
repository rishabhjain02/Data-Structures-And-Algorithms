"""

Another Count Rectangles
Problem Description
Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B. (Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)  


Problem Constraints
1 <= |A| <= 100000 1 <= A[i] <= 10^9 1 <= B <= 10^9  


Input Format
The first argument given is the integer array A. The second argument given is integer B.  


Output Format
Return the number of rectangles with distinct configurations with area less than B modulo (10^9 + 7).


Example Input
Input 1:
A = [1, 2]
B = 5
  Input 2:        
A = [1, 2]
B = 1
     


Example Output
Output 1:
 4
  Output 2:        
 1
     


Example Explanation
Explanation 1:
 
All 1X1, 2X2, 1X2 and 2X1 have area less than 5.
  Explanation 2:        
Only 1X1 is valid.

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        start = 0
        end = n-1
        count = 0
        B = B%(10**9+7)
        while(start <= end):
            if (A[start]*A[end]) >= B:
                end -= 1
            else:
                count = (count + 2*(end-start+1)-1)%(10**9+7)
                start += 1
        return count
