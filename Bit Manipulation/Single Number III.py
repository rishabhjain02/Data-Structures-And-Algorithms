"""

Single Number III
Problem Description
Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. Note: Output array must be sorted.  


Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 10^9


Input Format
First argument is an array of interger of size N.


Output Format
Return an array of two integers that appear only once.


Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
  Input 2:      
A = [1, 2]
    


Example Output
Output 1:
[3, 4]
  Output 2:      
[1, 2]
    


Example Explanation
Explanation 1:
 3 and 4 appear only once.
  Explanation 2:      
 1 and 2 appear only once.

"""

import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        # suppose a and b are two nos appearing once
        # Step1: XOR all no in arrays, it will give a^b
        xor = A[0]
        for i in range(1,len(A)):
            xor = xor^A[i]
            
        # Step2: find the position where a^b has a set bit
        pos = -1
        for i in range(math.ceil(math.log(max(A),2))):
            if (xor & (1<<i)) != 0:
                pos = i
                break
            
        # Step3: split the array into two array of no. having set bit at pos and the unset bit at pos
        xor0 = 0 # it will store the xor all the no. having unset bit at pos
        xor1 = 0 # it will store the xor all the no. having set bit at pos
        for i in range(len(A)):
            if (A[i] & (1<<pos)) != 0:
                xor1 = xor1^A[i]
            else:
                xor0 = xor0^A[i]
        
        # so finally xor0 will have one no. and xor1 and other no.        
        return [min(xor1, xor0), max(xor1, xor0)]
                
