"""

N integers containing only 1, 2 & 3
Problem Description

Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1, 2 and 3.

NOTE: All the A integers will fit in 32 bit integer.



Problem Constraints
1 <= A <= 29500



Input Format
The only argument given is integer A.



Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.



Example Input
Input 1:

 A = 3
Input 2:

 A = 7


Example Output
Output 1:

 [1, 2, 3]
Output 2:

 [1, 2, 3, 11, 12, 13, 21]


Example Explanation
Explanation 1:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.

"""

from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        count = 3
        queue = deque([1, 2, 3])
        ans = [1, 2, 3]
        
        while count < A:
            temp = queue.popleft()
            val1 = temp*10 + 1
            val2 = temp*10 + 2
            val3 = temp*10 + 3
            queue.append(val1)
            queue.append(val2)
            queue.append(val3)
            ans.append(val1)
            ans.append(val2)
            ans.append(val3)
            count += 3
            
        while len(ans) > A:
            ans.pop()
        
        return ans
