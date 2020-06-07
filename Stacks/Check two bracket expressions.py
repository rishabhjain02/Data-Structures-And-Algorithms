"""

Check two bracket expressions
Problem Description

Given two strings A and B. Each string represents an expression consisting of lowercase english alphabets, '+', '-', '(' and ')'.

The task is to compare them and check if they are similar. If they are similar return 1 else return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’ and every operand appears only once.



Problem Constraints
1 <= length of the each String <= 100



Input Format
The arguments given are string A and String B.



Output Format
Return 1 if they represent the same expression else return 0.



Example Input
Input 1:

 A = "-(a+b+c)"
 B = "-a-b-c"
Input 2:

 A = "a-b-(c-d)"
 B = "a-b-c-d"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 
Explanation 2:

 Both the expression are different.

"""

from collections import defaultdict

# Fuction to find actual sign of each operand in the expression
def get_signs(A):
    n = len(A)
    sign_map = defaultdict(int)
    stack = []
    operators = set(['+', '-', '(', ')'])
    sign = 1
    
    for i in range(n):

            if A[i] == '(':
                # if first element, just push the index of braces
                if i == 0:
                    stack.append(i)
                # else: check the sign at i-1: if -ve then revert the sign variable
                # and push index of braces
                else:
                    if A[i-1] == '-':
                        sign = sign * -1
                    stack.append(i)
                    
            # Here A[i] is operand        
            if A[i] not in operators:
                # if first element, just store the +ve sign(1) for the current operand in sign_map
                if i == 0:
                    sign_map[ord(A[i]) - ord('a')] = 1
                else:
                    # check sign at index just before the operand,
                    # If -ve: then store -1 * sign
                    # Here we are just multiplying the local sign of operand with the global sign
                    # present before opening braces.
                    if A[i-1] == '-':
                        sign_map[ord(A[i]) - ord('a')] = -1 * sign
                    # If +ve: then store sign
                    else:
                        sign_map[ord(A[i]) - ord('a')] = sign
                        
            if A[i] == ')':
                temp = stack.pop()
                # temp will be the opening braces, check sign at index just before this opening braces
                # if -ve then revert the sign variable
                if A[temp-1] == '-':
                    sign = sign * -1
    
    return sign_map
    
class Solution:
    # @param str1 : string
    # @param str2 : string
    # @return an integer
    def solve(self, str1, str2):
        
        # sign_map1 will store signs of operands a-z which are present in str1
        # sign_map2 will store signs of operands a-z which are present in str2
        sign_map1 = defaultdict(int)
        sign_map2 = defaultdict(int)
        
        sign_map1 = get_signs(str1)
        sign_map2 = get_signs(str2)
        
        # Checking sign at each index in both maps, if any index mismatch: return 0
        for i in range(26):
            if sign_map1[i] != sign_map2[i]:
                return 0
                
        return 1
