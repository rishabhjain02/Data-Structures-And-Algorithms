"""

K reverse linked list
Problem Description

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.



Problem Constraints
1 <= |A| <= 10^3

B always divides A



Input Format
The first argument of input contains a pointer to the head of the linked list.

The second arugment of input contains the integer, B.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:

 A = [1, 2, 3, 4, 5, 6]
 B = 3


Example Output
Output 1:

 [2, 1, 4, 3, 6, 5]
Output 2:

 [3, 2, 1, 6, 5, 4]


Example Explanation
Explanation 1:

 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]
Explanation 2:

 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]

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
	def reverseList(self, A, B):
	    cur = A
	    prev = None
	    next = None
	    count = 0
	    
	    if A == None:
	        return A
	    
	    while(cur != None and count < B):
	        next = cur.next
	        cur.next = prev
	        prev = cur
	        cur = next
	        count += 1
	        
	    A.next = self.reverseList(next, B)
	    return prev
