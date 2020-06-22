"""

Palindrome List
Problem Description

Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.



Problem Constraints
1 <= |A| <= 10^5



Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format
Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input
Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output
Output 1:

 1 
Output 2:

 0 


Example Explanation
Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

def check_palindrome(list1, list2):
    
    while(list1 != None and list2 != None):
        if list1.val != list2.val:
            return 0
        list1 = list1.next
        list2 = list2.next
    return 1

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
	    pointer = A
	    length = 0
	    while(pointer != None):
	        length += 1
	        pointer = pointer.next
	      
	    if length%2 == 0:
	        mid = length // 2
	    else:
	        mid = (length + 1) // 2
	        
	    count = 1
	    prev = None
	    cur = A
	    next = None
	    while count <= mid:
	        next = cur.next
	        cur.next = prev
	        prev = cur
	        cur = next
	        count += 1
	     
	    if length%2 == 0:
	        return check_palindrome(prev, cur)
	    else:
	        return check_palindrome(prev.next, cur)
	            
	        