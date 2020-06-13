"""

Infix to Postfix
Problem Description

Given string A denoting an infix expression. Convert the infix expression into postfix expression.

String A consists of ^, /, *, +, -, (, ) and lowercase english alphabets where lowercase english alphabets are operands and ^, /, *, +, - are operators.

Find and return the postfix expression of A.

NOTE:

^ has highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.


Problem Constraints
1 <= length of the string <= 500000



Input Format
The only argument given is string A.



Output Format
Return a string denoting the postfix conversion of A.



Example Input
Input 1:

 A = "x^y/(a*z)+b"
Input 2:

 A = "a+b*(c^d-e)^(f+g*h)-i"


Example Output
Output 1:

 "xy^az*/b+"
Output 2:

 "abcd^e-fgh*+^*+i-"


Example Explanation
Explanation 1:

 Ouput dentotes the postfix expression of the given input.

"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        precedence = {}
        ans = []
        stack = []
        precedence['('] = 1
        precedence['+'] = 2
        precedence['-'] = 2
        precedence['*'] = 3
        precedence['/'] = 3
        precedence['^'] = 4
        
        operators = set(['+', '-', '*', '/', '^'])
        brackets = set(['(', ')'])  
        
        for char in A:
            # If char is operand, add to ans
            if char not in operators and char not in brackets:
                ans.append(char)
            
            # If char is opening braces, push to operand stack
            elif char == '(':
                stack.append(char)
                
            # If char is closing braces, pop and add to ans untill opening braces is removed from stack     
            elif char == ')':
                val = stack.pop()
                while val != '(':
                    ans.append(val)
                    val = stack.pop()
                    
            # If char is operator, pop all the operators having precedence >= preced of char
            # and add them to ans and finally push the current char to stack.
            else:
                while stack != [] and precedence[stack[-1]] >= precedence[char]:
                    ans.append(stack.pop())
                stack.append(char)
                
        # Pop remaining operators from stack and add to ans
        while stack != []:
            ans.append(stack.pop())
            
        return "".join(ans)
                    
        
