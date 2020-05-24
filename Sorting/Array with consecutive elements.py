"""

Array with consecutive elements
Problem Description
Given an array of positive integers A, check and return whether the array elements are consecutive or not. NOTE: Try this with O(1) extra space.  


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9


Input Format
The only argument given is the integer array A.


Output Format
Return 1 if the array elements are consecutive else return 0.


Example Input
Input 1:
 A = [3, 2, 1, 4, 5]
Input 2:
 A = [1, 3, 2, 5]


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:
 As you can see all the elements are consecutive, so we return 1.
Explanation 2:
 Element 4 is missing, so we return 0.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        for i in range(1,n):
            if A[i] != A[i-1]+1:
                return 0
        return 1
      
        
    # Second approach --->
    # def solve(self, A):
    #     n = len(A)
    #     min_element = min(A)
    #     s = (n * (2*min_element + n-1)) // 2
    #     if s == sum(A):
    #         return 1
    #     return 0
