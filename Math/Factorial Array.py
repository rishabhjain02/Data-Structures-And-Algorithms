"""

Factorial Array
Problem Description
Groot has an array A of size N. Boring right? Groot thought so too, so he decided to construct another array B of the same size and defined elements of B as: B[i] = factorial of A[i] for every i such that 1<= i <= N.    
factorial of a number X denotes (1 x 2 x 3 x 4......(X-1) x (X)).
 Now Groot is interested in the total number of non-empty subsequences of array B such that every element in the subsequence has the same non empty set of prime factors. Since the number can be very large, return it modulo 10^9 + 7. NOTE: A set is a data structure having only distinct elements. Eg : the set of prime factors of Y=12 will be {2,3} and not {2,2,3}    


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^6
Your code will run against a maximum of 5 test cases.


Input Format
Only argument is an integer array A of size N.


Output Format
Return an integer deonting the total number of non-empty subsequences of array B such that every element in the subsequence has the same set of prime factors modulo 10^9+7.


Example Input
Input 1:
 A = [2, 3, 2, 3]
Input 2:
 A = [2, 3, 4]
   


Example Output
Output 1:
 6
Output 2:
 4
   


Example Explanation
Explanation 1:
 Array B will be : [2, 6, 2, 6]
 The total possible subsequences are 6 : [2], [2], [2, 2], [6], [6], [6, 6].
Input 2:
 Array B will be : [2, 6, 24]
 The total possible subsequences are 4 : [2], [6], [24], [6, 24].

"""

import math
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = max(A)
        prime = [1]*(n+1)
        prime[0] = 0
        prime[1] = 0
        primes_upto = defaultdict(int)
        primes_upto[0] = 0
        primes_upto[1] = 0
        primes_upto[2] = 1
        def seive(n):
            for i in range(2,int(math.sqrt(n))+1):
                if prime[i] == 1:
                    j = i
                    while(i*j<=n):
                        prime[i*j] = 0
                        j += 1
                    
        def count_primes(n):
            count = 0
            for i in range(3,n+1):
                if prime[i]:
                    primes_upto[i] = primes_upto[i-1]+1
                else:
                    primes_upto[i] = primes_upto[i-1]
            
        def find_ans():
            prime_upto_count = []
            factors_count = defaultdict(int)
            ans = 0
            for i in range(len(A)):
                if A[i] > 1:
                    factors_count[primes_upto[A[i]]] += 1
                
            for value in factors_count.values():
                ans += (2**value)-1
                
            return ans
                
        seive(n)
        count_primes(n)
        return find_ans()
        
                
                
        
