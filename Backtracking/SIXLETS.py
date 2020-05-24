"""

SIXLETS
Problem Description
Given a array of integers A of size N and an integer B. Return number of non-empty subsequences of A of size B having sum <= 1000.   


Problem Constraints
1 <= N <= 20 1 <= A[i] <= 1000 1 <= B <= N   


Input Format
The first argument given is the integer array A. The second argument given is the integer B.   


Output Format
Return number of subsequences of A of size B having sum <= 1000.


Example Input
Input 1:
    A = [1, 2, 8]
    B = 2
Input 2:
    A = [5, 17, 1000, 11]
    B = 4
  


Example Output
Output 1:
3
Output 2:
0
  


Example Explanation
Explanation 1:
 {1, 2}, {1, 8}, {2, 8}
 Explanation 1: 
 No valid subsequence

 """

 class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def sixlets(self, arr, B, cur_idx, n, ans, cur_sum, cur_set):
        
        if len(cur_set) == B:
            if cur_sum <= 1000:
                ans[0] += 1
            return
        
        
        if cur_idx == n:
            return
        
        
        cur_set.append(arr[cur_idx])
        self.sixlets(arr, B, cur_idx+1, n, ans, cur_sum+arr[cur_idx], cur_set)
        cur_set.pop()
        
        self.sixlets(arr, B, cur_idx+1, n, ans, cur_sum, cur_set)
    
    def solve(self, A, B):
        n = len(A)
        ans = [0]
        cur_set = []
        self.sixlets(A, B, 0, n, ans, 0, cur_set)
        return ans[0]
        
