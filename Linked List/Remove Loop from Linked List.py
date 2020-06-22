"""

Remove Loop from Linked List
Problem Description

Given a linked list which contains some loop.

You need to find the node, which creates a loop, and break it by making the node point to NULL.



Problem Constraints
1 <= number of nodes <= 1000



Input Format
Only argument is the head of the linked list.



Output Format
return the head of the updated linked list.



Example Input
Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL


Example Explanation
Explanation 1:

 Chain of 1->2 is broken.
Explanation 2:

 Chain of 4->6 is broken.

"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def find_cycle_start(head):
    slow_pointer = head
    fast_pointer = head
    meeting_node = None
    
    # Finding meeting point of slow and fast pointer, using while True bcz there must be a loop
    # as mentioned in the question
    while True:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            meeting_node = slow_pointer
            break
    
    # Start p1 from head and p2 from meeting point    
    pointer1 = head
    pointer2 = meeting_node
    
    # Where p1 = p2 that will be our cycle_start_node
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        # Finding cycle_start_node
        cycle_start_node = find_cycle_start(A)
        
        # start a pointer from cycle_start_node
        pointer = cycle_start_node
        
        # Finding the node which is pointing to the cycle_start_node
        while pointer.next != cycle_start_node:
            pointer = pointer.next
        
        # Make the next of that node as None to break the loop
        pointer.next = None
        
        return A
        
