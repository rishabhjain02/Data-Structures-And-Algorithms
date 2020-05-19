"""

Permutations
Problem Description
Given an integer array A of size N denoting collection of numbers , return all possible permutations. NOTE:   
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
   


Problem Constraints
1 <= N <= 9


Input Format
Only argument is an integer array A of size N.


Output Format
Return a 2-D array denoting all possible permutation of the array.


Example Input
A = [1, 2, 3]


Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3] 
  [2, 3, 1] 
  [3, 1, 2] 
  [3, 2, 1] ]


Example Explanation
All the possible permutation of array [1, 2, 3].
	
"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	
	def permutation(self, cur_index, n, arr, ans):
	        if cur_index == n-1:
	            ans.append(arr[0:n])
	            return
	        
	        for i in range(cur_index, n):
	            arr[i], arr[cur_index] = arr[cur_index], arr[i]
	            self.permutation(cur_index+1, n, arr, ans)
	            arr[i], arr[cur_index] = arr[cur_index], arr[i]
	
	def permute(self, arr):
	    ans = []
	    n = len(arr)
	    self.permutation(0, n, arr, ans)
	    return ans
