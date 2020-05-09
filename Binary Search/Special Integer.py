"""

Special Integer
Problem Description
Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.


Problem Constraints
1 <= |A| <= 100000 1 <= A[i] <= 10^9 1 <= B <= 10^9


Input Format
The first argument given is the integer array A. The second argument given is integer B.  


Output Format
Return the maximum value of K (sub array length).


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 10
  Input 2:        
A = [5, 17, 100, 11]
B = 130
     


Example Output
Output 1:
 2
  Output 2:        
 3
     


Example Explanation
Explanation 1:
Constraints are satisfied for maximal value of 2.
  Explanation 2:        
Constraints are satisfied for maximal value of 3.

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
    	# This function return true if all the subsets of length x has sum<=B
        def check(x):
            left = 0
            right = x
            s = 0
            for i in range(x):
                s+=A[i]
            if s>B:
                return False
            while(right<len(A)):
                s -= A[left]
                s += A[right]
                if s>B:
                    return False
                left += 1
                right += 1
            return True
            
        low = 1
        high = len(A)
        ans = 0
        while(low <= high):
            x = low + (high-low)//2
            if check(x):
                ans = x
                low = x+1
            else:
                high = x-1
        
        if ans == 0:
            return 1
        return ans
                
