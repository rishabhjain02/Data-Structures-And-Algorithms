"""

Count Right Triangles
Problem Description

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

NOTE: The answer may be large so return the answer modulo (10^9 + 7).



Problem Constraints
1 <= N <= 10^5

0 <= A[i], B[i] <= 10^9



Input Format
The first argument given is an integer array A.
The second argument given is the integer array B.



Output Format
Return the number of unordered triplets that form a right angled triangle modulo (109 + 7).



Example Input
Input 1:

 A = [1, 1, 2]
 B = [1, 2, 1]
Input 2:

 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]


Example Output
Output 1:

 1
Output 2:

 6


Example Explanation
Explanation 1:

 All three points make a right angled triangle. So return 1.
Explanation 2:

 6 quadruplets which make a right angled triangle are: (1, 1), (1, 2), (2, 2)
                                                       (1, 1), (3, 1), (1, 2)
                                                       (1, 1), (3, 1), (3, 2)
                                                       (2, 1), (3, 1), (3, 2)
                                                       (1, 1), (1, 2), (3, 2)
                                                       (1, 2), (3, 1), (3, 2)

"""

from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ans = 0
        x_map = defaultdict(int)
        y_map = defaultdict(int)
        
        # make the freq maps for x coordinates and y coordinates 
        for i in range(n):
            x_map[A[i]] += 1
            y_map[B[i]] += 1
            
        # find the no. of points having same x-coordinate to cur_point or same y-coordinate to cur_point 
        for i in range(n):
            x_freq = x_map[A[i]]
            y_freq = y_map[B[i]]
            
            # multiply both the freq. excluding the cur_point x-coordinate and y-coordinate and add to ans
            ans = (ans + (x_freq - 1) * (y_freq - 1))%(10**9+7)
        
        return ans
