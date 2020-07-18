"""

Binary updates
Problem Description

Given an integer A denoting the size of the array consisting all ones.

You are given Q queries, for each query there are two integer x and y:

If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: There will atleast 1 query where value of x is 1.



Problem Constraints
1 <= A, Q <= 10^5

0 <= x <= 1

1 <= y <= A



Input Format
First argument is an integer A denoting the size of array.

Second argument is a 2-D array B of size Q x 2 where B[i][0] denotes x and B[i][1] denotes y.



Output Format
Return an integer array denoting the output of each query where x is 1.



Example Input
Input 1:

 A = 4
 B = [ [1, 2],
       [0, 2],
       [1, 4] ]
Input 2:

 A = 5
 B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ] 


Example Output
Output 1:

 [2, -1]
Output 2:

 [5, -1]


Example Explanation
Explanation 1:

 Initially array = [1, 1, 1, 1]. For first query 2nd one is at index 2.
 After Second query array becomes [1, 0, 1, 1].
 For third query there is no 4th one.
Explanation 2:

 Initially array = [1, 1, 1, 1, 1]. After first query array becomes [1, 1, 0, 1, 1].
 For second query 4th one is at index 5.    
 After third query array remains same [1, 1, 0, 1, 1].
 For fourth query there is no 5th one.

"""


def build_segment_tree(st, start, end, pos):
    if start == end:
        st[pos] = 1
        return
        
    mid = (start + end)//2    
    
    build_segment_tree(st, start, mid, 2*pos+1)
    build_segment_tree(st, mid+1, end, 2*pos+2)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]


def update(st, start, end, index, pos):
    if start == end and start == index:
        st[pos] = 0
        return
        
    mid = (start + end)//2
        
    if index <= mid:
        update(st, start, mid, index, 2*pos+1)
    else:
        update(st, mid+1, end, index, 2*pos+2)
    
    st[pos] = st[2*pos+1] + st[2*pos+2]
    
    
def count_one(st, start, end, k, pos):
    if end-start+1 == st[pos]:
        return start+k
    
    if start == end:
        return -1
    
    mid = (start + end)//2
    
    if st[2*pos+1] >= k:
        return count_one(st, start, mid, k, 2*pos+1)
    else:
        return count_one(st, mid+1, end, k-st[2*pos+1], 2*pos+2)
    

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = A
        st = [0 for i in range(4*n)]
        ans = []
        
        build_segment_tree(st, 0, n-1, 0)
        
        for query in B:
            if query[0] == 0:
                update(st, 0, n-1, query[1]-1, 0)
            else:
                if query[1] > st[0]:
                    ans.append(-1)
                else:
                    ans.append(count_one(st, 0, n-1, query[1], 0))
                
        return ans
        
