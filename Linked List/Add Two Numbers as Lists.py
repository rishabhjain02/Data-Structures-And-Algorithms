"""

Add Two Numbers as Lists
Problem Description

You are given two linked lists, A and B representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.



Problem Constraints
1 <= |A|, |B| <= 10^5



Input Format
The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format
Return a pointer to the head of the required linked list.



Example Input
Input 1:

 
 A = [2, 4, 3]
 B = [5, 6, 4]
Input 2:

 
 A = [9, 9]
 B = [1]


Example Output
Output 1:

 
 [7, 0, 8]
Output 2:

 
 [0, 0, 1]


Example Explanation
Explanation 1:

 A = 342 and B = 465. A + B = 807. 
Explanation 2:

 A = 99 and B = 1. A + B = 100. 

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
	def addTwoNumbers(self, A, B):
	    # Creating a temporary dummy node
	    head = ListNode(0)
	    first = A
	    second = B
	    carry = 0
	    cur = head
	    
	    while(first != None and second != None):
	        s = first.val + second.val + carry
	        carry = s // 10
	        temp = ListNode(s%10)
	        cur.next = temp
	        cur = cur.next
	        first = first.next
	        second = second.next
	    
	    # If items remaining in first list
	    while first != None:
	        s = first.val + carry
	        carry = s // 10
	        temp = ListNode(s%10)
	        cur.next = temp
	        cur = cur.next
	        first = first.next
	        
	    # If items remaining in second list
	    while second != None:
	        s = second.val + carry
	        carry = s // 10
	        temp = ListNode(s%10)
	        cur.next = temp
	        cur = cur.next
	        second = second.next
	        
	    # if carry is greater than zero after computing last element, we have to make one extra node 
	    # for that carry
	    if carry > 0:
	        temp = ListNode(carry)
	        cur.next = temp
	    
	    return head.next
    	        
    	    
	                
