"""

Merge Two Sorted Lists
Problem Description

Merge two sorted linked lists A and B and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.



Problem Constraints
0 <= |A|, |B| <= 10^5



Input Format
The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format
Return a pointer to the head of the merged linked list.



Example Input
Input 1:

 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15
Input 2:

 A = 1 -> 2 -> 3
 B = Null


Example Output
Output 1:

 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2:

 1 -> 2 -> 3


Example Explanation
Explanation 1:

 Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20 
Explanation 2:

 We don't need to merge as B is empty. 

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
	    first = A
	    second = B
	    cur = None
	    head = None
	    
	    if A.val <= B.val:
	        head = A
	        first = A.next
	        cur = A
	    else:
	        head = B
	        second = B.next
	        cur = B
	        
	    while(first != None and second != None):
	        if first.val <= second.val:
	            cur.next = first
	            first = first.next
	        else:
	            cur.next = second
	            second = second.next
	        cur = cur.next
	            
	    if first != None:
	        cur.next = first
	    if second != None:
	        cur.next = second
	    
	    return head
	    
	    
