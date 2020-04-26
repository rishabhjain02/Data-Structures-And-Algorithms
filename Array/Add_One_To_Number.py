"""

Add One To Number
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). The digits are stored such that the most significant digit is at the head of the list. NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, following are some good questions to ask :
Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
   


Problem Constraints
1 <= size of the array <= 1000000


Input Format
First argument is an array of digits.


Output Format
Return the array of digits after adding one.


Example Input
Input 1:
[1, 2, 3]
   


Example Output
Output 1:
[1, 2, 4]
   


Example Explanation
Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 1:
            if A[0]+1 > 9:
                A[0] = (A[0]+1)%10
            else:
                A[0] = A[0]+1
                return A
            return [1]+A
            
        count_zeros = 0
        for i in range(len(A)-1):
            if A[i] == 0 and A[i+1] == 0:
                count_zeros += 1
            else:
                break
        if A[0] == 0 and count_zeros == 0:
            A = A[1:]
        if count_zeros > 0:
            A = A[count_zeros+1:]
        
        carry = 0
        if A[-1]+1 > 9:
            carry = 1
            A[-1] = (A[-1]+1)%10
        else:
            A[-1] = A[-1]+1
            return A
            
        for i in range(len(A)-2,-1,-1):
            if A[i]+carry > 9:
                A[i] = (A[i]+carry)%10
                carry = 1
            else:
                A[i] = A[i] + carry
                return A
        return [1]+A
            