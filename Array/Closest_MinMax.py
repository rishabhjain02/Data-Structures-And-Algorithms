"""

Closest MinMax
Given an array of size N. Find the size of the smallest subarray such that it contains atleast one occurrence of the maximum value of the array and atleast one occurrence of the minimum value of the array. Constraints:
1.   1 <= N <= 2000
Input Format An integer array. Output Format Length of the smallest subarray which has atleast one occurrence of minimum and maximum element of the array Example Input
Array:[1 3 5 2 4 3]
Example Output
3
Explanation Choose the subarray starting from the 0th index and ending at 2nd index which is of size 3.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_value = max(A)
        min_value = min(A)
        last_min = -1
        last_max = -1
        ans = len(A)
        
        for i in range(len(A)):
            if A[i] == max_value:
                if last_min != -1:
                    ans = min(ans, i-last_min+1)
                last_max = i
            
            if A[i] == min_value:
                if last_max != -1:
                    ans = min(ans, i-last_max+1)
                last_min = i
        return ans
