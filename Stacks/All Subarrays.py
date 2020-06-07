"""

All Subarrays
Problem Description

Given an integer array A of size N. You have to generate it's all subarrays having the size greater than 1.

Then for each subarray find Bitwise XOR of its maximum and second maximum element.

Find and return the maximum value of XOR among all subarrays.



Problem Constraints
2 <= N <= 10^5

1 <= A[i] <= 10^7



Input Format
Only argument is an integer array A.



Output Format
Return an integer, i.e maximum value of XOR of maximum and 2nd maximum element among all subarrays.



Example Input
Input 1:

 A = [2, 3, 1, 4]
Input 2:

 A = [1, 3]


Example Output
Output 1:

 7
Outnput 2:

 2


Example Explanation
Explanation 1:

 All subarrays of A having size greater than 1 are:
 Subarray            XOR of maximum and 2nd maximum no.
 1. [2, 3]           1
 2. [2, 3, 1]        1
 3. [2, 3, 1, 4]     7
 4. [3, 1]           2
 5. [3, 1, 4]        7
 6. [1, 4]           5
So maximum value of Xor among all subarrays is 7.
Explanation 2:

 Only subarray is [1, 3] and XOR of maximum and 2nd maximum is 2.

"""



# Approach:
# We are assuming current element as the 2nd max and then, 
# finding nearest left maximum for each element and store that in left array, if not found store 0
# and nearest right maximum for each element and store that in right array, if not found store 0
# then find max XOR (xor1) by taking xor of all elements of A and left array.
# similarly find max XOR (xor2) by taking xor of all elements of A and right array.
# Our ans will be the max(xor1, xor2)


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        stack = []
        left = [0]*n
        right = [0]*n
        
        
        # Finding nearest left max
        
        stack.append(A[0])
        
        for i in range(1, n):
            # if top > A[i]: top will be max and push A[i] to stack
            if stack != [] and stack[-1] > A[i]:
                left[i] = stack[-1]
                stack.append(A[i])
            
            else:
                # Pop elements till we get top > A[i] or stack become empty
                while(stack != [] and stack[-1] <= A[i]):
                    stack.pop()
                # If stack is not empty then, top will be the max    
                if stack != []:
                    left[i] = stack[-1]
                # if Stack is empty then, put 0 as max    
                else:
                    left[i] = 0
                    
                stack.append(A[i])
        
        
        # Finding nearest right max similarly as left max
        
        stack = []        
        stack.append(A[n-1])
        
        for i in range(n-2, -1, -1):
            if stack != [] and stack[-1] > A[i]:
                right[i] = stack[-1]
                stack.append(A[i])
            
            else:
                while(stack != [] and stack[-1] <= A[i]):
                    stack.pop()
                if stack != []:
                    right[i] = stack[-1]
                else:
                    right[i] = 0
                    
                stack.append(A[i])
                
        xor1 = 0
        xor2 = 0
        
        for i in range(n):
            if left[i] != 0:
                xor1 = max(xor1, left[i]^A[i])
                
        for i in range(n):
            if right[i] != 0:
                xor2 = max(xor2, right[i]^A[i])
                
        return max(xor1, xor2)
        
