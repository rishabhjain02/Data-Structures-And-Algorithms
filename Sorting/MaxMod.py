"""

MaxMod
Problem Description
Given an array A of size N, groot wants you to pick 2 indices i and j such that
1 <= i, j <= N
A[i] % A[j] is maximum among all possible pairs of (i, j).
Help Groot in finding the maximum value of A[i] % A[j] for some i, j.     


Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 100000


Input Format
First and only argument in an integer array A.


Output Format
Return an integer denoting the maximum value of A[i] % A[j] for any valid i, j.


Example Input
Input 1:
 A = [1, 2, 44, 3]
Input 2:
 A = [2, 6, 4]
   


Example Output
Output 1:
 3
Output 2:
 4
   


Example Explanation
Explanation 1:
 For i = 3, j = 2  A[i] % A[j] = 3 % 44 = 3.
 No pair exists which has more value than 3.
Explanation 2:
 For i = 2, j = 1  A[i] % A[j] = 4 % 6 = 4.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        max_no = A[n-1]
        less_than_max = 0

        # here we have to find largest and second largest number
        for i in range(n-2, -1, -1):
            if A[i] != max_no:
                less_than_max = A[i]
                break
                
        return less_than_max%max_no

