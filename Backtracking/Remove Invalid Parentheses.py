"""

Remove Invalid Parentheses
Problem Description
Given a string A consisting of lowercase English alphabets and parentheses '(' and ')'. Remove the minimum number of invalid parentheses in order to make the input string valid.  Return all possible results. You can return the results in any order. 


Problem Constraints
1 <= length of the string <= 20


Input Format
The only argument given is string A.


Output Format
Return all possible strings after removing the minimum number of invalid parentheses.


Example Input
Input 1:
 A = "()())()"
Input 2:
 A = "(a)())()"


Example Output
Output 1:
 ["()()()", "(())()"]
Output 2:
 ["(a)()()", "(a())()"]


Example Explanation
Explanation 1:
 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 4 then string becomes : "()()()"
        2. Remove the parentheses at index 2 then string becomes : "(())()"
Explanation 2:
 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 5 then string becomes : "(a)()()"
        2. Remove the parentheses at index 2 then string becomes : "(a())()"

"""

class Solution:
    
    def remove(self, s, count_left, count_right, cur_idx, count_to_remove, curr, ans, open, close, temp_set):
        
        if (count_right > count_left) or (count_to_remove < 0):
            return 
        
        if cur_idx == len(s):
            if count_left == count_right:
                temp_str = "".join(curr)
                if temp_str not in temp_set:
                    ans.append(temp_str)
                    temp_set.add(temp_str)
            return
              
        c = s[cur_idx]
        curr.append(c)
        
        if c == open:
            self.remove(s, count_left+1, count_right, cur_idx+1, count_to_remove, curr, ans, open, close, temp_set)
            
        elif c == close:
            self.remove(s, count_left, count_right+1, cur_idx+1, count_to_remove, curr, ans, open, close, temp_set)
            
        elif c != open and c != close:
            self.remove(s, count_left, count_right, cur_idx+1, count_to_remove, curr, ans, open, close, temp_set)
        
        
        curr.pop()
        self.remove(s, count_left, count_right, cur_idx+1, count_to_remove-1, curr, ans, open, close, temp_set)
    
    
    def solve(self, A):
        ans = []
        open = '('
        close = ')'
        count_left = 0
        count_right = 0
        count_to_remove = 0
        
        for i in range(len(A)):
            if A[i] == open:
                count_left += 1
            if A[i] == close:
                if count_left > 0:
                    count_left -= 1
                else:
                    count_right += 1
        
        count_to_remove = count_left + count_right
        curr = []
        temp_set = set()
        self.remove(A, 0, 0, 0, count_to_remove, curr, ans, open, close, temp_set)
        return ans






# Second Approach --->


# class Solution:
#     # @param A : string
#     # @return a list of strings
    
#     def remove(self, s, start, last_removed, ans, paren):
#         count = 0
#         for i in range(start, len(s)):
#             if s[i] == paren[0]:
#                 count += 1
#             if s[i] == paren[1]:
#                 count -= 1
#             if count < 0 :
#                 for j in range(last_removed, i+1):
#                     if (s[j] == paren[1] and (j == 0 or s[j-1] != paren[1])):
#                         self.remove(s[:j]+s[j+1:], i, j, ans, paren)
#                 return
            
#         s = s[::-1]
        
#         if paren[0] == '(':
#             self.remove(s, 0, 0, ans, (')', '('))
#         else:
#             ans.append(s)
    
#     def solve(self, A):
#         ans = []
#         self.remove(A, 0, 0, ans, ('(', ')'))
#         return ans
