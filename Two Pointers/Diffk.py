"""

Diffk
Given an array 'A' of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
 Example: Input : 
    A : [1 3 5] 
    k : 4
 Output : YES as 5 - 1 = 4 

Return 0 / 1 ( 0 for false, 1 for true ) for this problem Try doing this in less than linear space complexity.

"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
	    n = len(A)
	    start = 0
	    end = 1
	    while(end<n):
	        if start == end:
	            end += 1
	            
	        elif A[end]-A[start] > B:
	            start += 1
	            
	        elif A[end]-A[start] < B:
	            end += 1
	           
	        else:
	            return 1
	    
	    return 0
	            
	
