"""

Count of divisors for multiple queries
Problem Description
Given an array of integers A, find and return the count of divisors of each element of the array. NOTE: Order of the resultant array should be same as the input array.     


Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^6


Input Format
The only argument given is the integer array A.


Output Format
Return the count of divisors of each element of the array in the form of an array.


Example Input
Input 1:
 A = [2, 3, 4, 5]
Input 2:
 A = [8, 9, 10]


Example Output
Output 1:
 [2, 2, 3, 2]
Output 1:
 [4, 3, 4]


Example Explanation
Explanation 1:
 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:
 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].

"""

import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_num = max(A)
        ans = []
        spf = [i for i in range(max_num+1)]
        
        i = 2
        while(i*i<=max_num):
            if spf[i] == i:
                j = i*i
                while(j<=max_num):
                    spf[j] = i
                    j += i
            i += 1    
        
        
        for i in range(len(A)):
            num = A[i]
            r = 1
            while(num>1):
                p = spf[num]
                c = 0
                while(num%p == 0):
                    c += 1
                    num = num//p
                r *= c + 1
            ans.append(r)
    
        return ans        
            