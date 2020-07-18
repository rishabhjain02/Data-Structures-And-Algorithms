"""

Range Minimum Query
Problem Description

Given an integer array A of size N.

You have to perform two types of query, in each query you are given three integers x,y,z.

If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.



Problem Constraints
1 <= N, M <= 10^5

1 <= A[i] <= 10^9

If x = 0, 1<= y <= N and 1 <= z <= 10^9

If x = 1, 1<= y <= z <= N



Input Format
First argument is an integer array A of size N.

Second argument is a 2-D array B of size M x 3 denoting queries.



Output Format
Return an integer array denoting the output of each query where value of x is 1.



Example Input
Input 1:

 A = [1, 4, 1]
 B = [ 
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2] 
     ]
Input 2:

 A = [5, 4, 5, 7]
 B = [ 
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output
Output 1:

 [1, 4]
Output 2:

 [4, 2]


Example Explanation
Explanation 1:

 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.
Explanation 2:

 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.

"""


def build_segment_tree(A, st, start, end, pos):
    if start == end:
        st[pos] = A[start]
        return
        
    mid = (start + end)//2    
    
    build_segment_tree(A, st, start, mid, 2*pos+1)
    build_segment_tree(A, st, mid+1, end, 2*pos+2)
    
    st[pos] = min(st[2*pos+1], st[2*pos+2])
    
    
def update(A, st, start, end, index, new_val, pos):
    if start == end and start == index:
        st[pos] = new_val
        return
        
    mid = (start + end)//2
        
    if index <= mid:
        update(A, st, start, mid, index, new_val, 2*pos+1)
    else:
        update(A, st, mid+1, end, index, new_val, 2*pos+2)
    
    st[pos] = min(st[2*pos+1], st[2*pos+2])
    

def range_min(A, st, range_start, range_end, start, end, pos):
    if range_start <= start and range_end >= end:
        return st[pos]
        
    if range_start > end or range_end < start:
        return float("inf")
        
    mid = (start + end)//2
    
    return min(range_min(A, st, range_start, range_end, start, mid, 2*pos+1), range_min(A, st, range_start, range_end, mid+1, end, 2*pos+2))


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        ans = []
        st = [float("inf") for i in range(4*n)]
        
        build_segment_tree(A, st, 0, n-1, 0)
        
        for query in B:
            if query[0] == 0:
                update(A, st, 0, n-1, query[1]-1, query[2], 0)
            else:
                ans.append(range_min(A, st, query[1]-1, query[2]-1, 0, n-1, 0))
        
        return ans
        
        
        
