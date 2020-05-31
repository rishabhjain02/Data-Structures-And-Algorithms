"""

Equal
Problem Description

Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P,Q,R & S are integers values in the array

NOTE:

1) Return the indices 'A1 B1 C1 D1', so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices in the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2


Problem Constraints
1 <= N <= 1000

0 <= A[i] <= 1000



Input Format
Single argument which is an integer array A of size N.



Output Format
Return an array of size 4 which indexes of values P,Q,R and S.



Example Input
Input 1:

 A = [3, 4, 7, 1, 2, 9, 8]
Input 2:

 A = [2, 5, 1, 6]


Example Output
Output 1:

 [0, 2, 3, 5]
Output 2:

 [0, 1, 2, 3]


Example Explanation
Explanation 1:

 A[0] + A[2] = A[3] + A[5]
 Note: indexes returned should be 0-based.
Explanation 2:

 A[0] + A[1] = A[2] + A[3]

"""

from collections import defaultdict
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def equal(self, A):
	    n = len(A)
        hash = defaultdict(int)
        p, q, r, s = float("inf"), float("inf"), float("inf"), float("inf")
        
        for i in range(n):
            for j in range(i+1, n):
                sum = A[i] + A[j]
                if sum in hash:
                    prev = hash[sum]
                    if (prev[0],prev[1],i,j) < (p,q,r,s) and prev[0]<i and prev[1]!=i and prev[1]!=j:
                        p,q,r,s = prev[0],prev[1],i,j
                    
                else:
                    hash[sum] = (i, j)
        
        return [p,q,r,s]
