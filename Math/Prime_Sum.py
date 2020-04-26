"""

Prime Sum
Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.   If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.     


Problem Constraints
4 <= A <= 2*10^7


Input Format
First and only argument of input is an even number A.


Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.


Example Input
 4


Example Output
 [2, 2]


Example Explanation
 There is only 1 solution for A = 4.

"""

import math
class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
	    def SOE(n,prime):
	        prime[0] = prime[1] = False
	        for i in range(2,int(math.sqrt(n))+1):
	            if prime[i] == 1:
	                j=i
	                while(i*j<=n):
	                    prime[i*j] = 0
	                    j += 1
	        return prime
	    
	    prime = [1]*(A+1)
	    prime = SOE(A,prime)
	    ans = []
	    for i in range(A):
	        if prime[i] and prime[A-i]:
	            ans.append(i)
	            ans.append(A-i)
	            break
	    return ans
	        