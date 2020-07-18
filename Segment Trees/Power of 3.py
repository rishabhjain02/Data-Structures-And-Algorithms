"""

Power of 3
Problem Description

Given a binary string A of size N and an integer matrix B of size Q x 3.

Matrix B has Q queries:

For queries of type B[i][0] = 1, flip the value at index B[i][1] in A if and only if the value at that index is 0 and return -1.
For queries of type B[i][0] = 0, Return the value of the binary string from index B[i][1] to B[i][2] modulo 3.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints
1 <= N <= 100000
1 <= Q <= 200000
1 <= B[i][1], B[i][2] <= N
B[i][1] <= B[i][2]



Input Format
The first argument given is the string A.
The second argument given is the integer matrix B of size Q * 3.



Output Format
Return an array of size Q where ith value is answer to ith query.



Example Input
Input 1:

 A = 10010
 B = [  [0, 3, 5]
        [0, 3, 4]
        [1, 2, -1]
        [0, 1, 5]
     ]
Input 2:

 A = 11111
 B = [
        [0, 2, 4]
        [1, 2, -1
        [0, 2, 4]]
     ]


Example Output
Output 1:

 [2, 1, -1, 2]
Output 2:

 [1, -1, 1]


Example Explanation
Explanation 1:

 For query 1, binary string from index 3 to 5 is 010 = 2. So 2 mod 3 = 2.
 For query 2, binary string from index 3 to 4 is 01 = 1. So 1 mod 3 = 1.
 After query 3, given string changes to 11010.
 For query 4, binary string from index 1 to 5 is 11010 = 26. So 26 mod 3 = 2.
 So, output array is [2, 1, -1, 2].
Explanation 2:

 For query 1, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 After query 2, string remains same as there is already 1 at index 2.
 For query 3, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 So, output array is [1, -1, 1].
 

"""


import math

def build_segment_tree(A, st, start, end, pos):
    if start == end:
        st[pos] = A[start]
        return 
    
    mid = (start + end)//2
    
    build_segment_tree(A, st, start, mid, 2*pos+1)
    build_segment_tree(A, st, mid+1, end, 2*pos+2)
    
    st[pos] = ((st[2*pos+1]%3 * pow(2, end-mid, 3))%3 + st[2*pos+2]%3)%3
    
    
def flip(A, st, start, end, index, pos):
    if start == end and start == index:
        st[pos] = 1
        return 
    
    mid = (start + end)//2
    
    if index <= mid:
        flip(A, st, start, mid, index, 2*pos+1)
    else:
        flip(A, st, mid+1, end, index, 2*pos+2)
    
    st[pos] = ((st[2*pos+1]%3 * pow(2, end-mid, 3))%3 + st[2*pos+2]%3)%3


def get_value(st, range_start, range_end, start, end, pos):
    if start == range_start and end == range_end:
        return st[pos]
        
    mid = (start + end)//2
    
    if range_start <= mid:
        if range_end <= mid:
            return get_value(st, range_start, range_end, start, mid, 2*pos+1)%3
        else:
            left = get_value(st, range_start, mid, start, mid, 2*pos+1)
            right = get_value(st, mid+1, range_end, mid+1, end, 2*pos+2)
            
            return ((left * pow(2, range_end-mid, 3))%3 + right%3)%3
    
    else:
        return get_value(st, range_start, range_end, mid+1, end, 2*pos+2)%3

class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, s, B):
        ans = []
        A = []
        for c in s:
            A.append(int(c))
        n = len(A)
        st = [float("inf") for i in range(4*n)]
        
        build_segment_tree(A, st, 0, n-1, 0)
        
        for query in B:
            if query[0] == 0:
                ans.append(get_value(st, query[1]-1, query[2]-1, 0, n-1, 0))
            else:
                flip(A, st, 0, n-1, query[1]-1, 0)
                ans.append(-1)
                
        return ans
        