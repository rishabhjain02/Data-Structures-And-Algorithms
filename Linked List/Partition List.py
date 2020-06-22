"""

Partition List
Problem Description

Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.

You should preserve the original relative order of the nodes in each of the two partitions.



Problem Constraints
1 <= |A| <= 10^6

1 <= A[i], B <= 10^9



Input Format
The first argument of input contains a pointer to the head to the given linked list.

The second argument of input contains an integer, B.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

A = [1, 4, 3, 2, 5, 2]
B = 3
Input 2:

A = [1, 2, 3, 1, 3]
B = 2


Example Output
Output 1:

[1, 2, 2, 4, 3, 5]
Output 2:

[1, 1, 2, 3, 3]


Example Explanation
Explanation 1:

 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2:

 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):
	    
	    smaller_start = None
	    smaller_end = None
	    greater_start = None
	    greater_end = None
	    
	    cur = A
	    while cur != None:
	        if cur.val < B:
	            if smaller_start == None:
	                smaller_start = cur
	                smaller_end = cur
	            else:
	                smaller_end.next = cur
	                smaller_end = cur
	        
	        else:
	            if greater_start == None:
	                greater_start = cur
	                greater_end = cur
	            else:
	                greater_end.next = cur
	                greater_end = cur
	            
	        cur = cur.next
	    
	    if smaller_start == None:
	        return greater_start
	        
	    if greater_start == None:
	        smaller_end.next = None
	        return smaller_start
	    
	    greater_end.next = None
	    smaller_end.next = greater_start
	    return smaller_start
