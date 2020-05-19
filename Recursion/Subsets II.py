"""

Subsets II
Problem Description
Given a collection of integers denoted by array A of size N that might contain duplicates, return all possible subsets. NOTE:  
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
    


Problem Constraints
0 <= N <= 16


Input Format
Only argument is an integer array A of size N.


Output Format
Return a 2-D vector denoting all the possible subsets.


Example Input
Input 1:
 A = [1, 2, 2]
Input 2:
 A = [1, 1]


Example Output
Output 1:
 [
    [],
    [1],
    [1, 2],
    [1, 2, 2],
    [2],
    [2, 2]
 ]
Output 2:
 [
    [],
    [1],
    [1, 1]
 ]


Example Explanation
Explanation 1:
All the subsets of the array [1, 2, 2] in lexicographically sorted order.

"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def findsubsets(self, cur_index, cur_set, ans, A, s):
	    
	    if cur_index == len(A):
	        temp1 = sorted(cur_set)
	        temp2 = tuple(temp)
	        if temp2 not in s:
	            ans.append(temp)
	            s.add(temp2)
	        return
	    
	    self.findsubsets(cur_index+1, cur_set, ans, A, s)
        cur_set.append(A[cur_index])
        self.findsubsets(cur_index+1, cur_set, ans, A, s)
        cur_set.pop()
            
	def subsetsWithDup(self, A):
	    ans = []
	    cur_set = []
	    s=set()
	    self.findsubsets(0, cur_set, ans, A, s)
	    ans.sort()
	    return ans
	    
