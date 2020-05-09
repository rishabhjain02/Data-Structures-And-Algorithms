"""

Christmas Trees
Problem Description
You are given an aray A consisting of heights of Christmas trees, and an array B of same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br. You are to choose 3 such trees such that they have the minimum cost, find the minimum cost. If not possible to choose 3 such trees, return -1.     


Problem Constraints
1 <= A[i], B[i] <= 10^9
3 <= size(A) = size(B) <= 3000


Input Format
First argument is an integer array A.
Second argument is an integer array B.


Output Format
Return an integer denoting the minimum cost of choosing 3 trees whose heights are strictly in increasing order, if not possible, -1.


Example Input
Input 1:
 A = [1, 3, 5]
 B = [1, 2, 3]
Input 2:
 A = [1, 6, 4, 2, 6, 9]
 B = [2, 5, 7, 3, 2, 7]
  


Example Output
Output 1:
 6 
Output 2:
 7 
  


Example Explanation
Explanation 1:
 We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6. 

"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pair_sum = 0
        ans = float("inf")
        n = len(A)
        for i in range(1,n-1):
            left_min = float("inf")
            right_min = float("inf")
            for j in range(i):
                if A[j]<A[i]:
                    left_min = min(left_min,B[j])
            for j in range(i+1,n):
                if A[j]>A[i]:
                    right_min = min(right_min,B[j])
            ans = min(ans,left_min+B[i]+right_min)        
        if ans == float("inf"):
            return -1
        return ans
        
