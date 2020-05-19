"""

All Unique Permutations
Problem Description
Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations. NOTE: No 2 entries in the permutation sequence should be the same.
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
      


Problem Constraints
1 <= |A| <= 9


Input Format
Only argument is an integer array A of size N.


Output Format
Return a 2-D array denoting all possible unique permutation of the array.


Example Input
Input 1:
A = [1, 1, 2]
  Input 2:                
A = [1, 2]
         


Example Output
Output 1:
[ [1,1,2]
  [1,2,1]
  [2,1,1] ]
  Output 2:                
[ [1, 2]
  [2, 1] ]
         


Example Explanation
Explanation 1:
 All the possible unique permutation of array [1, 1, 2].
  Explanation 2:                
 All the possible unique permutation of array [1, 2].

"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	
	def permutation(self, cur_index, n, arr, ans):
	        if cur_index == n-1:
	            ans.append(arr[0:n])
	            return
	            
	        s = set()
	        for i in range(cur_index, n):
	            if arr[i] not in s:
    	            arr[i], arr[cur_index] = arr[cur_index], arr[i]
    	            self.permutation(cur_index+1, n, arr, ans)
    	            arr[i], arr[cur_index] = arr[cur_index], arr[i]
    	            s.add(arr[i])
	
	def permute(self, arr):
	    ans = []
	    n = len(arr)
	    self.permutation(0, n, arr, ans)
	    return ans
