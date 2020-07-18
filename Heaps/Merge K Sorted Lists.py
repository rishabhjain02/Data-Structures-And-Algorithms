"""

Merge K Sorted Lists
Problem Description

Given a list containing head pointers of N sorted linked lists. Merge these N given sorted linked lists and return it as one sorted list.



Problem Constraints
1 <= total number of elements in given linked lists <= 100000



Input Format
First and only argument is a list containing N head pointers.



Output Format
Return a pointer to the head of the sorted linked list after merging all the given linked lists.



Example Input
Input 1:

 1 -> 10 -> 20
 4 -> 11 -> 13
 3 -> 8 -> 9
Input 2:

 10 -> 12
 13
 5 -> 6


Example Output
Output 1:

 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
Output 2:

 5 -> 6 -> 10 -> 12 ->13


Example Explanation
Explanation 1:

 The resulting sorted Linked List formed after merging is 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20.
Explanation 2:

 The resulting sorted Linked List formed after merging is 5 -> 6 -> 10 -> 12 ->13.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        heap = []
        n = len(A)
        
        for i in range(n):
            node = A[i]
            heapq.heappush(heap, (node.val, i))
                
        ans = ListNode(0)
        head = ans
        
        while len(heap) > 0:
            val, index = heapq.heappop(heap)
            node = A[index]
            head.next = node
            head = head.next
            
            if node.next:
                node = node.next
                A[index] = node
                heapq.heappush(heap, (node.val, index))
                
        return ans.next
        
        