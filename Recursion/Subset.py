"""

Subset
Problem Description
Given a set of distinct integers, A, return all possible subsets. NOTE:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
    


Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.


Output Format
Return a vector of vectors denoting the answer.


Example Input
Input 1:
A = [1]
  Input 2:            
A = [1, 2, 3]
       


Example Output
Output 1:
[
    []
    [1]
]
  Output 2:            
[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]
       


Example Explanation
Explanation 1:
 You can see that these are all possible subsets.
  Explanation 2:            
You can see that these are all possible subsets.

"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	
	def findsubsets(self, cur_index, cur_set, ans, A):
	    if cur_index == len(A):
	        ans.append(cur_set[:])
	        return
	        
	    self.findsubsets(cur_index+1, cur_set, ans, A)
	    
	    cur_set.append(A[cur_index])
	    self.findsubsets(cur_index+1, cur_set, ans, A)
	    cur_set.pop()
	
	def subsets(self, A):
	    A.sort()
	    ans = []
	    cur_set = []
	    self.findsubsets(0, cur_set, ans, A)
	    ans.sort()
	    return ans
