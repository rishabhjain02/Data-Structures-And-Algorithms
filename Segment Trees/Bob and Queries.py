"""

Bob and Queries
Problem Description

Bob has an array A of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.

You have to perform three types of query, in each query you are given three integers x, y and z.

if x = 1: Update the value of A[y] to 2 * A[y] + 1.
if x = 2: Update the value A[y] to ⌊A[y]/2⌋ , where ⌊⌋ is Greatest Integer Function.
if x = 3: Take all the A[i] such that y <= i <= z and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints
1 <= N, Q <= 100000
1 <= y, z <= N
1 <= x <= 3



Input Format
The first argument has the integer A.
The second argument is a 2d matrix B, of size Q x 3, representing the queries.



Output Format
Return an array of integers where ith index represents the answer of the ith type 3 query.



Example Input
Input 1:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]   
        [3, 1, 3] 
        [3, 2, 4]   
     ]
Input 2:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [3, 1, 3]
        [2, 1, -1]
        [3, 1, 3]   
     ]


Example Output
Output 1:

 [3, 2]
Output 2:

 [2, 1]


Example Explanation
Explanation 1:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 After query 3, A => [1, 1, 1, 0, 0]
 For query 4, Concatenation of Binary String between index 1 and 3 : 111. So, number of 1's = 3
 For query 5, Concatenation of Binary String between index 2 and 4 : 110. So, number of 1's = 2
 So, output array is [3, 2].
Explanation 2:

 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 For query 3, Concatenation of Binary String between index 1 and 3 : 110. So, number of 1's = 2
 After query 4, A => [0, 1, 0, 0, 0]
 For query 5, Concatenation of Binary String between index 2 and 4 : 010. So, number of 1's = 1.
 So, output array is [2, 1].

"""


def update1(A, st, start, end, index, pos):
    if start == end and start == index:
        st[pos] += 1
        return
        
    mid = (start + end)//2
        
    if index <= mid:
        update1(A, st, start, mid, index, 2*pos+1)
    else:
        update1(A, st, mid+1, end, index, 2*pos+2)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]
    
def update2(A, st, start, end, index, pos):
    if start == end and start == index:
        st[pos] -= 1
        st[pos] = max(0, st[pos])
        return
        
    mid = (start + end)//2
        
    if index <= mid:
        update2(A, st, start, mid, index, 2*pos+1)
    else:
        update2(A, st, mid+1, end, index, 2*pos+2)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]
    
def range_count(A, st, range_start, range_end, start, end, pos):
    if range_start <= start and range_end >= end:
        return st[pos]
        
    if range_start > end or range_end < start:
        return 0
        
    mid = (start + end)//2
    
    return range_count(A, st, range_start, range_end, start, mid, 2*pos+1) + range_count(A, st, range_start, range_end, mid+1, end, 2*pos+2)



class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = A
        st = [0 for i in range(4*n)]
        ans = []
        
        for query in B:
            if query[0] == 1:
                update1(A, st, 0, n-1, query[1]-1, 0)
            elif query[0] == 2:
                update2(A, st, 0, n-1, query[1]-1, 0)
            else:
                ans.append(range_count(A, st, query[1]-1, query[2]-1, 0, n-1, 0))
                
        return ans
        
        
