"""

Ways to form Max Heap 2
Problem Description

Max heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.

Given an array A of size N consisting of N - 1 distinct elements. In other words there is exactly one element that is repeated.
It is given that the element that would repeat would be either the maximum element or the minimum element.

Find the number of structurally different Max heaps possible using all the N elements of the array i.e. Max heap of size N.

As final answer can be very large return your answer modulo 10^9 + 7.



Problem Constraints
1 <= N <= 1000



Input Format
First and only argument is an integer array A.



Output Format
Return an integer denoting the number of structurally different Max heaps possible modulo 109 + 7.



Example Input
Input 1:

 A = [1, 5, 5]
Input 2:

 A = [2, 2, 7]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 The possible max heaps using the given elements are:- First: 5 on the root. 1 as the left child of root and 5 as the right child of the root.   
                5
              /   \
            1       5
 Second: 5 on the root. 5 as the left child of root and 1 as the right child of the root.
                5
              /   \
            5       1            
Explanation 2:

 There is only one possible max heaps: 7 on the root. 2 as the left child of root and 2 as the right child of the root.   
                7
              /   \
            2       2

"""


import math

def nCr(n,r):
    f = math.factorial
    if n < 0 or r < 0 or (n-r) < 0:
        return 0
    return f(n) // f(r) // f(n-r)

# Function to calculate ways for distinct elements
def ways_max(n):
    mod = 10**9+7
    if n == 0 or n == 1 or n == 2:
        return 1
    if n < 0:
        return 0
        
    height = int(math.log2(n))
    # x is no. of elements till second last level
    x = (2**height - 1)
    left_nodes = (x-1)//2 + min(n-x, (x+1)//2)
    right_nodes = n - 1 - left_nodes
    
    return (nCr(n-1, left_nodes)%mod * ways_max(left_nodes)%mod * ways_max(right_nodes)%mod)%mod
    
# Function to calculate ways when minimum element occurs two times    
def ways_min(n):
    mod = 10**9+7
    if n == 0 or n == 1 or n == 2:
        return 1
    if n < 0:
        return 0
        
    height = int(math.log2(n))
    # x is no. of elements till second last level
    x = (2**height - 1)
    left_nodes = (x-1)//2 + min(n-x, (x+1)//2)
    right_nodes = n - 1 - left_nodes
    
    # Case1: When one min element is present is left tree and other min in right tree
    case1 = (nCr(n-3, left_nodes-1)%mod * ways_max(left_nodes)%mod * ways_max(right_nodes)%mod)%mod
    
    # Case2: When both are in left tree 
    case2 = (nCr(n-3, left_nodes-2)%mod * (ways_min(left_nodes))%mod * ways_max(right_nodes)%mod)%mod 
    
    # Case3: When both are in right tree
    case3 = (nCr(n-3, left_nodes)%mod * ways_max(left_nodes)%mod * (ways_min(right_nodes))%mod)%mod
    
    return (case1 + case2 + case3)%mod


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = max(A)
        n = len(A)
        
        # if Max element occurs two times
        if A.count(mx) == 2:
            return ways_max(n)
            
        return ways_min(n)
        
