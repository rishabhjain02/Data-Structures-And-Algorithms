"""

Maximum Absolute Difference
Problem Description
You are given an array of N integers, A1, A2, .... AN.

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.


Problem Constraints
1 <= N <= 100000 -10^9 <= A[i] <= 10^9   


Input Format
First argument is an integer array A of size N.


Output Format
Return an integer denoting the maximum value of f(i, j).


Example Input
Input 1:
A=[1, 3, -1]
  


Example Output
Output 1:
5
  


Example Explanation
Explanation 1:
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = A[0]
        min1 = A[0]
        max2 = A[0]
        min2 = A[0]
        for i in range(len(A)):
            case1 = A[i] + i
            max1 = max(max1,case1)
            min1 = min(min1,case1)
            case2 = A[i] - i
            max2 = max(max2,case2)
            min2 = min(min2,case2)
            
        return max((max1 - min1), (max2 - min2))
