"""

Number of Squareful Arrays
Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square. Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[ i ] != A2[ i ]. 
Input Format
The only argument given is the integer array A.
Output Format
Return the number of permutations of A that are squareful.
Constraints
1 <= length of the array <= 12
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [2, 2, 2]
Output 1:
    1

Input 2:
    A = [1, 17, 8]
Output 2:
    2

"""

import math
class Solution:
    # @param A : list of integers
    # @return an integer
    
    
    def squarefull(self,x,y):
        num = x+y
        if num == (int(math.sqrt(num)) * int(math.sqrt(num))):
            return True
        return False
    
    def permutation(self, cur_index, n, arr, ans, prev):
	        if cur_index == n:
	            ans[0] += 1
	            return
	            
	        s = set()
	        for i in range(cur_index, n):
	            if arr[i] not in s and (self.squarefull(prev, arr[i]) or cur_index == 0):
	                temp = prev
	                prev = arr[i]
	                arr[i], arr[cur_index] = arr[cur_index], arr[i]
	                self.permutation(cur_index+1, n, arr, ans, prev)
	                arr[i], arr[cur_index] = arr[cur_index], arr[i]
	                s.add(arr[i])
	                prev = temp
	                
    
    def solve(self, arr):
        ans = [0]
	    n = len(arr)
	    temp = []
	    if n == 1:
	        return 0
	    self.permutation(0, n, arr, ans, 0)
	    return ans[0]
        
        
