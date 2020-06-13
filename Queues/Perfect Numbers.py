"""

Perfect Numbers
Problem Description

Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



Problem Constraints
1 <= A <= 100000



Input Format
The only argument given is an integer A.



Output Format
Return a string that denotes the Ath Perfect Number.



Example Input
Input 1:

 A = 2
Input 2:

 A = 3


Example Output
Output 1:

 22
Output 2:

 1111


Example Explanation
Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221

"""

from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        count = 2
        queue = deque(['1', '2'])
        perfect_list = ['1', '2']
        
        while count < A:
            temp = queue.popleft()
            queue.append(temp + '1')
            queue.append(temp + '2')
            perfect_list.append(temp + '1')
            perfect_list.append(temp + '2')
            count += 2
            
        value = perfect_list[A-1]
        perfect_number = value + value[::-1]
        return perfect_number
 