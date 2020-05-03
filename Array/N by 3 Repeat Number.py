"""

N/3 Repeat Number
You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space. If so, return the integer. If not, return -1. If there are multiple solutions, return any one. Example :
Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        me1 = A[0]
        c1 = 1
        me2 = 0
        c2 = 1
        j = 0
        for i in range(1,n):
            if A[i] == me1:
                c1 += 1
            else:
                me2 = A[i]
                j = i+1
                break
        for i in range(j,n):
            if A[i] == me1:
                c1 += 1
            elif A[i] == me2:
                c2 += 1
            else:
                if c1 == 0:
                    me1 = A[i]
                    c1 = 1
                elif c2 == 0:
                    me2 = A[i]
                    c2 = 1
                else:
                    c1 -= 1
                    c2 -= 1
        
        c1 = 0
        c2 = 0
        for i in range(n):
            if A[i] == me1:
                c1 += 1
            if A[i] == me2:
                c2 += 1
                
        if c1>n//3:
            return me1
        elif c2>n//3:
            return me2
        else:
            return -1
                
                
                
                

