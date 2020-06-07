"""

Sort stack using another stack
Problem Description

Given a stack of integers A, sort it using another stack.

Return the array of integers after sorting the stack using another stack.



Problem Constraints
1 <= |A| <= 5000

0 <= A[i] <= 1000000000



Input Format
The only argument given is the integer array A.



Output Format
Return the array of integers after sorting the stack using another stack.



Example Input
Input 1:

 A = [5, 4, 3, 2, 1]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 [1, 2, 3, 4, 5]
Output 2:

 [5, 11, 17, 100]


Example Explanation
Explanation 1:

 Just sort the given numbers.
Explanation 2:

 Just sort the given numbers.

"""

def empty(stack):
    return stack == []

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, stack1):
        stack2 = []
        stack3 = []
        
        while(not empty(stack1)):
            value = stack1.pop()
            stack2.append(value)
            
        while(not empty(stack2)):
            value = stack2.pop()
            
            if empty(stack1):
                stack1.append(value)
                
            else:
                while (not empty(stack1)) and (stack1[-1] > value):
                    temp = stack1.pop()
                    stack3.append(temp)
                stack1.append(value)
                
                while(not empty(stack3)):
                    temp = stack3.pop()
                    stack1.append(temp)
        
        return stack1        
                
                