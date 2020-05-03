"""

Max Distance
Problem Description
Given an array A of integers of size N. Find the maximum of value of j - i such that A[i] <= A[j].             


Problem Constraints
1 <= N <= 1000000 -10^9 <= A[i] <= 10^9          


Input Format
First argument is an integer array A of size N.


Output Format
Return an integer denoting the maximum value of j - i.


Example Input
Input 1:
A = [3, 5, 4, 2]
           


Example Output
Output 1:
2
           


Example Explanation
Explanation 1:
For A[0] = 3 and A[2] = 4, the ans is (2 - 0) = 2. 

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        data = []  
        for i in range(n):
            data.append([i+1,A[i]])
            
        data.sort(key = lambda x: x[1])
        
        ans = 0
        
        l_min = [0]*n
        l_min[0] = data[0][0]
        for i in range(1,n):
            l_min[i] = min(l_min[i-1], data[i][0])
            
        for i in range(n):
            ans = max(ans,data[i][0]-l_min[i])
            
        return ans
