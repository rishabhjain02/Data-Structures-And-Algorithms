"""

Longest Palindromic List
Problem Description

Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.

A palindrome list is a list that reads the same backward and forward.

Expected memory complexity : O(1)



Problem Constraints
1 <= length of the linked list <= 2000

1 <= Node value <= 100



Input Format
The only argument given is head pointer of the linked list.



Output Format
Return the length of the longest palindrome list.



Example Input
Input 1:

 2 -> 3 -> 3 -> 3
Input 2:

 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2


Example Output
Output 1:

 3
Output 2:

 5


Example Explanation
Explanation 1:

 3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:

 2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.


"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def get_palindrome_length(list1, list2):
    count = 0
    
    while(list1 != None and list2 != None):
        if list1.val == list2.val:
            count += 1
        else:
            break
        list1 = list1.next
        list2 = list2.next
    return count

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        prev = None
        cur = A
        next = None
        result = float("-inf")
        
        while cur != None:
            next = cur.next
            cur.next = prev
            
            # Getting count for odd length palindrome i.e. considering cur as middle element
            result = max(result, 2 * get_palindrome_length(prev, next) + 1)
            
            # Getting count for even length palindrome i.e. considering partition as middle element
            result = max(result, 2 * get_palindrome_length(cur, next))
            
            prev = cur
            cur = next
            
        return result
