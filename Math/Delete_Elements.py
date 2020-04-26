"""

Delete Elements
Problem Description
Given an integer array A of size N.
Find the minimum number of elements that need to be removed such that the GCD of the resulting array becomes 1.

If not possible then return -1.
    


Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 1e9
    


Input Format
Input contains a single integer array A
   


Output Format
Return an integer


Example Input
Input 1:
 A = [7, 2, 5]
   


Example Output
Output 1:
 0
   


Example Explanation
Explanation 1:
 GCD of the array A is 1.
 so, the number of elements to be removed is 0.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return -1
        def gcd(a,b):
            if b == 0:
                return abs(a)
            return gcd(b,a%b)
        ans = gcd(A[0],A[1])
        for i in range(2,len(A)):
            ans = gcd(ans,A[i])
        
        if ans == 1:
            return 0
        return -1
        
