"""

Merge Two Sorted Arrays
Problem Description
Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.


Problem Constraints
-10^10 <= A[i],B[i] <= 10^10


Input Format
First Argument is a 1-D array representing A. Second Argument is also a 1-D array representing B.    


Output Format
Return a 1-D vector which you got after merging A and B.


Example Input
Input 1:
A = [4, 7, 9 ]
B = [2 ,11, 19 ]
  Input 2:          
A = [1]
B = [2]
      


Example Output
Output 1:
[2, 4, 7, 9, 11, 19]
  Output 2:          
[1, 2]
      


Example Explanation
Explanation 1:
Merging A and B produces the output as described above.
  Explanation 2:          
 Merging A and B produces the output as described above.

"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        ans = []
        i = 0
        j = 0
        while(i < n and j < m):
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j += 1
        
        while(i<n):
            ans.append(A[i])
            i += 1
            
        while(j<m):
            ans.append(B[j])
            j += 1
            
        return ans
            
