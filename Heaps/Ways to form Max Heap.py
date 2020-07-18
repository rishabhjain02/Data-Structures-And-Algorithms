"""

Ways to form Max Heap
Problem Description

Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.

Find the number of distinct Max Heap can be made from A distinct integers.

In short, you have to ensure the following properties for the max heap :

Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.)
Every node is greater than all its children.
NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 109 + 7.



Problem Constraints
1 <= A <= 100



Input Format
First and only argument is an inetegr A.



Output Format
Return an integer denoting the number of distinct Max Heap.



Example Input
Input 1:

 A = 4
Input 2:

 A = 10


Example Output
Output 1:

 3
Output 2:

 3360


Example Explanation
Explanation 1:

 Let us take 1, 2, 3, 4 as our 4 distinct integers
 Following are the 3 possible max heaps from these 4 numbers :
      4           4                     4
    /  \         / \                   / \ 
   3    2   ,   2   3      and        3   1
  /            /                     /    
 1            1                     2
Explanation 2:

 Number of distinct heaps possible with 10 distinct integers = 3360.

"""


import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def ways(n):
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
    
    return (nCr(n-1, left_nodes)%mod * ways(left_nodes)%mod * ways(right_nodes)%mod)%mod
    
class Solution:
	# @param A : integer
	# @return an integer
	def solve(self, A):
	    return ways(A)
	    
	    
