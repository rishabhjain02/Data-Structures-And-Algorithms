"""

Count the primes
Problem Description

Given an array A, containing positive integers. You need to perform some queries on it.

You will be given Q Queries. Each query will have one string and two integers. Each Query can be of two type :

"C" X Y - Here "C" says that we need to Change the integer at position X to integer Y.
"A" X Y - Here "A" say that we are Asked number of primes in the the range : [X, Y] (inclusive)
For each Query of type 2, you need to calculate an integer denoting the answer to it.

NOTE:

Assume 1-indexing for all queries.
Your code will be run on multiple test cases (< 10). Make sure to come up with an optimised solution and take care of clearing global variables.


Problem Constraints
1 <= Size of A <= 4 * 10^4

1 <= A[i] <= 10^6

1 <= Number of Queries (Size of B, C, D) <= 5 * 10^4



Input Format
First argument is an integer array A.
Second argument is a string array B.
Third argument is an integer array C.
Fourth argument is an integer array D.

In the i-th query, B[i] dentotes the string, C[i] denotes X and D[i] denotes Y.



Output Format
Return an integer array, where each of the element represents the answer to the queries of type 2, in chronological order.



Example Input
Input 1:

 A = [1, 3, 121, 20, 17, 26, 29]
 B = ["A", "C", "A"]
 C = [1, 3,  1]
 D = [7, 19, 7]
Input 2:

 A = [7, 15, 11]
 B = ["C", "A"]
 C = [2, 2]
 D = [9, 3]


Example Output
Output 1:

 [3, 4]
Input 2:

 [1]


Example Explanation
Explanation 1:

 Given array A = [1, 3, 121, 20, 17, 26, 29]. Let's list down queries:
 1. A 1 7 :  Number of primes in complete array [1-7] is 3 => 3, 17, 29
 2. C 3 19 : Change the number at index-3 to 19. So Array becomes : [1, 3, 19, 20, 17, 26, 29]
 3. A 1 7 : Number of primes in complete array [1-7] is 4 => 3, 19, 17, 29
 So output : [3, 4]
Explanation 2:

 Given array A = [7, 15, 11]. Let's list down queries:
 1. C 2 9 :  Change the number at index-2 to 9. So Array becomes : [7, 9, 11]
 2. A 2 3 : Number of primes in array [2 - 3] is 1 => 11
 So output : [1]

"""


import math

def sieve(prime, max_no):
    prime[0] = 0
    prime[1] = 0
    
    for i in range(2, int(math.sqrt(max_no))+1):
        if prime[i]:
            j = i
            while i*j <= max_no:
                prime[i*j] = 0
                j += 1


def build_segment_tree(A, st, start, end, pos, prime):
    if start == end:
        st[pos] = prime[A[start]]
        return
        
    mid = (start + end)//2    
    
    build_segment_tree(A, st, start, mid, 2*pos+1, prime)
    build_segment_tree(A, st, mid+1, end, 2*pos+2, prime)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]


def change(A, st, start, end, index, new_val, pos, prime):
    if start == end and start == index:
        st[pos] = prime[new_val]
        return
        
    mid = (start + end)//2
        
    if index <= mid:
        change(A, st, start, mid, index, new_val, 2*pos+1, prime)
    else:
        change(A, st, mid+1, end, index, new_val, 2*pos+2, prime)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]
    
    
def range_primes(A, st, range_start, range_end, start, end, pos):
    if range_start <= start and range_end >= end:
        return st[pos]
        
    if range_start > end or range_end < start:
        return 0
        
    mid = (start + end)//2
    
    return range_primes(A, st, range_start, range_end, start, mid, 2*pos+1) + range_primes(A, st, range_start, range_end, mid+1, end, 2*pos+2)



class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @param C : list of integers
    # @param D : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D):
        n = len(A)
        m = len(B)
        ans = []
        st = [float("inf") for i in range(4*n)]
        
        max_no = 10**6
        prime = [1]*(max_no+1)
        sieve(prime, max_no)
        
        build_segment_tree(A, st, 0, n-1, 0, prime)
        
        for i in range(m):
            if B[i] == "C":
                change(A, st, 0, n-1, C[i]-1, D[i], 0, prime)
            else:
                ans.append(range_primes(A, st, C[i]-1, D[i]-1, 0, n-1, 0))
                
        return ans
        
        
