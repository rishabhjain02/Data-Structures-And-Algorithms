"""

Count Subarrays
Problem Description
Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements. Since the number of subarrays could be large, return value % 109 +7.  


Problem Constraints
1 <= N <= 10^5 1 <= A[i] <= 10^6   


Input Format
The only argument given is an Array A, having N integers.


Output Format
Return the number of subarrays of A, that have unique elements.


Example Input
Input 1:
 A = [1, 1, 3]
Input 2:
 A = [2, 1, 2]


Example Output
Output 1:
 4
Output 1:
 5


Example Explanation
Explanation 1:
 Subarrays of A that have unique elements only:
 [1], [1], [1, 3], [3]
Explanation 2:
 Subarrays of A that have unique elements only:
 [2], [1], [2, 1], [1, 2], [2]

"""

from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        left = 0
        right = 0
        count = defaultdict(int)
        
        while (right<n):
            if count[A[right]] == 0:
                count[A[right]] = 1
                right += 1
            else:
                ans = (ans + (right-left))%(10**9+7)
                count[A[left]] = 0
                left += 1
        
        # for remaining elements we can find using n*(n+1)/2        
        ans = (ans + ((n-left)*(n-left+1)//2))%(10**9+7)
        return ans
