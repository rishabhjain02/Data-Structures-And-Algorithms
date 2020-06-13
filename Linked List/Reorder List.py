"""

Reorder List
Problem Description

Given a singly linked list A

 A: A0 → A1 → … → An-1 → An 
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.



Problem Constraints
1 <= |A| <= 10^6



Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output
Output 1:

 [1, 5, 2, 4, 3] 
Output 2:

 [1, 4, 2, 3] 


Example Explanation
Explanation 1:

 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:

 The array will be arranged to [A0, An, A1, An-1, A2].

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

def find_mid(A):
    slow_pointer = A
    fast_pointer = A
    while(fast_pointer != None and fast_pointer.next != None and fast_pointer.next.next != None):
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer
    
    
def reverse_list(head):
    cur = head
    prev = None
    next = None
    while(cur != None):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
    
    
def merge_lists(first, second):
    head = first
    p = first
    flag = 1
    first = first.next
    
    while(first != None and second != None):
        if flag == 1:
            p.next = second
            second = second.next
        else:
            p.next = first
            first = first.next
        p = p.next
        flag = flag * -1
    
    if first != None:
        p.next = first
    
    if second != None:
        p.next = second
        
    return head


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
	    midpoint = find_mid(A)
	    secondlist_start = reverse_list(midpoint.next)
	    midpoint.next = None
	    return merge_lists(A, secondlist_start)
	    
	    
	    
	    
	    
