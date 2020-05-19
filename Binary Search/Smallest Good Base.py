"""

Smallest Good Base
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format. 
Input Format
The only argument given is the string representing A.
Output Format
Return the smallest good base of A in string format.
Constraints
3 <= A <= 10^18
For Example
Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).

"""

import math
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        N = int(A)
        def findValue(b,digits):
            # to find the value in decimal from base b with digits no. of 1
            # so it is sum of gp: b^0 + b^1 + b^2 +.....+ b^(digits-1)
            value = ((b**digits)-1)//(b-1)
            return value
            
        def findBase(digits):  # Range of base can be [2, N-1] as minimum value of N is 3
            low = 2
            high = N-1
            while(low<=high):
                mid = low+(high-low)//2 
                value = findValue(mid,digits)
                if value == N:
                    return mid
                elif value < N:
                    low = mid+1
                else:
                    high = mid-1
            return 0
            
            
        # maximum no. of 1111...... can be upto 64 for possible range of N i.e. [3, 10**18]
        for digits in range(64,0,-1):  
            ans = findBase(digits)
            if ans:
                return str(ans)
