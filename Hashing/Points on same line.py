"""

Points on same line
Problem Description

Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane.

Find and return the maximum number of points which lie on the same line.



Problem Constraints
1 <= (length of the array A = length of array B) <= 1000

-10^5 <= A[i], B[i] <= 10^5



Input Format
First argument is an integer array A.
Second argument is an integer array B.



Output Format
Return the maximum number of points which lie on the same line.



Example Input
Input 1:

 A = [-1, 0, 1, 2, 3, 3]
 B = [1, 0, 1, 2, 3, 4]
Input 2:

 A = [3, 1, 4, 5, 7, -9, -8, 6]
 B = [4, -8, -3, -2, -1, 5, 7, -4]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}.
Explanation 2:

 Any 2 points lie on a same line.

"""

import math
from collections import defaultdict

# Function to find GCD
def gcd(A, B):
    if B == 0:
        return abs(A)
    return gcd(B,A%B)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        max_val = float("-inf") # Variable to keep track of max frequency
        
        for i in range(n-1):
            x1, y1 = A[i], B[i]
            hash = defaultdict(int) # Hashmap <y2-y2, x2-x1> <frequency>
            temp = 0
            for j in range(i+1,n):
                x2, y2 = A[j], B[j]
                if x1 == x2 and y1 == y2: # If both points are equal
                    temp += 1
                else:
                    if x2-x1 == 0:     # Infinite slope
                        hash["inf"] += 1
                    elif y2-y1 == 0:
                        hash["zero"] += 1 # Zero slope
                    else:
                        gcd1 = gcd(y2-y1, x2-x1)
                        val1 = (y2-y1)//gcd1
                        val2 = (x2-x1)//gcd1
                        if val1 < 0 and val2 > 0:
                            hash[(val1, val2*-1)] += 1
                        elif val2 < 0 and val1 > 0:
                            hash[(val1*-1, val2)] += 1
                        else:
                            hash[(abs(val1), abs(val2))] += 1
            
            cur_max = max(hash.values()) # Finding max value from hashmap
            cur_max += temp
            max_val = max(max_val, cur_max) # Updating global max
        
        return max_val+1
