"""

Clone a Linked List
Problem Description

Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a single link list) while the second pointer, however, can point to any node in the list and not just the previous node.

You have to create a copy of this list and return the head pointer of the duplicated list.



Problem Constraints
1 <= length of the list <= 100000

1 <= Value of node <= 100000



Input Format
The only argument given is head pointer of the doubly linked list.



Output Format
Return the head pointer of the duplicated list.



Example Input
Input 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Input 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


Example Output
Output 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Output 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


Example Explanation
Explanation 1:

 Just clone the given list.
Explanation 2:

 Just clone the given list

"""

"""
class ListNode: 
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""
def clonelist(A):
    original = A
    while original != None:
        new = ListNode(original.val)
        new.next = original.next
        original.next = new
        original = original.next.next
        
    original = A
    while original != None:
        original.next.random = original.random.next
        original = original.next.next
    
    original = A
    deep_copy = A.next
    temp = A.next
    while original != None and original.next != None and temp.next != None:
        original.next = original.next.next
        temp.next = temp.next.next
        original = original.next 
        temp = temp.next
        
    return deep_copy
    
