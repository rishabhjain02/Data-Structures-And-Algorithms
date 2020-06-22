"""

Swap List Nodes in pairs
Problem Description

Given a linked list A, swap every two adjacent nodes and return its head.

NOTE: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.



Problem Constraints
1 <= |A| <= 10^6



Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = 1 -> 2 -> 3 -> 4
Input 2:

 A = 7 -> 2 -> 1


Example Output
Output 1:

 2 -> 1 -> 4 -> 3
Output 2:

 2 -> 7 -> 1


Example Explanation
Explanation 1:

 In the first example (1, 2) and (3, 4) are the adjacent nodes. Swapping them will result in 2 -> 1 -> 4 -> 3
Explanation 2:

 In the second example, 3rd element i.e. 1 does not have an adjacent node, so it won't be swapped. 

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None


# Solution 1:

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
	    if A == None or A.next == None:
	        return A
	    head = A.next
	    cur = A
	    pointer1 = A
	    pointer2 = None
	    
	    while(cur != None and cur.next != None):
	        pointer2 = cur.next
	        pointer1.next = pointer2
	        cur.next = pointer2.next
	        pointer2.next = cur
	        pointer1 = cur
	        cur = cur.next
	        
	    return head
	    

# Solution 2:

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        start = ListNode('dummy')
        start.next = A
        current = start
        while current.next and current.next.next:
            current.next = self.swap(current.next, current.next.next)
            current = current.next.next
        return start.next

    def swap(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2