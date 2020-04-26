"""

Sorted Permutation Rank
Problem Description
Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated. Note: The answer might not fit in an integer, so return your answer % 1000003 


Problem Constraints
1 <= len(A) <= 1000


Input Format
First argument is a string A.


Output Format
Return an integer denoting the rank of the given string.


Example Input
Input 1:
A = "acb"


Example Output
Output 1:
2


Example Explanation
Explanation 1:
Given A = "acd".
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.


"""

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
	    def fact(n):
	        p=1
	        for i in range(2,n+1):
	            p = p*i
	        return p
	    
	    count_max = [0]*len(A)
	    
	    def right_max(count_max,A):
	        for i in range(len(A)-1):
	            for j in range(i+1,len(A)):
	                if A[j]<A[i]:
	                    count_max[i] += 1
	                    
	    right_max(count_max,A)
	    l = len(A)
	    f_fact = fact(l-1)
	    
	    rank = 0
	    
	    for i in range(l-1):
	        rank += (count_max[i]*f_fact)
	        f_fact = f_fact//(l-i-1)
	        
	    rank += (count_max[-1])
	   
	    return (rank+1)%1000003
	    
	        
	   
	    
