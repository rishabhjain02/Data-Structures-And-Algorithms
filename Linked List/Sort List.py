"""

Sort List
Problem Description

Sort a linked list, A in O(n log n) time using constant space complexity.



Problem Constraints
0 <= |A| = 10^5



Input Format
The first and the only arugment of input contains a pointer to the head of the linked list, A.



Output Format
Return a pointer to the head of the sorted linked list.



Example Input
Input 1:

A = [3, 4, 2, 8]
Input 2:

A = [1]


Example Output
Output 1:

[2, 3, 4, 8]
Output 2:

[1]


Example Explanation
Explanation 1:

 The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2:

 The sorted form of [1] is [1].

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

def getMid(head):
    if head == None:
        return head
    
    slow = head
    fast = head
    
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        
    return slow
    
def merge(A, B):
    if A == None:
        return B
    if B == None:
        return A
        
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

def mergeSort(head):
    if head == None or head.next == None:
        return head
    
    mid = getMid(head)
    mid_next = mid.next
    mid.next = None
    
    left = mergeSort(head)
    right = mergeSort(mid_next)
    
    return merge(left, right)

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
	    A = mergeSort(A)
	    return A
	    
