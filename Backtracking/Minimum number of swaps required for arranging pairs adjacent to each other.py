"""

Minimum number of swaps required for arranging pairs adjacent to each other
Problem Description
There are A pairs and therefore 2A people. Each person has a unique number ranging from 1 to 2A. An array of integers B shows the arrangement of these 2A people. A matrix C of size A x 2 is given describing pairs i.e. people that are partner of each other. C[i][0] and C[i][1] are partner of each other. Find the minimum number of swaps required to arrange these pairs such that all pairs become adjacent to each other.  


Problem Constraints
1 <= A <= 20 1 <= B[i] <= 2*A C[i][0]!=C[i][1] 1 <= C[i][0], C[i][1] <= 2*A  


Input Format
The First argument given is an integer A. The Second argument given is the integer array B. The Third argument given is matrix C.  


Output Format
Return the minimum number of swaps required to arrange these pairs such that all pairs become adjacent to each other.


Example Input
Input 1:
A = 3
B = [3, 5, 6, 4, 1, 2]
C = [   [1, 3]
        [2, 6]
        [4, 5]  ]
  Input 2:          
A = 1
B = [1, 2]
C = [ [1, 2] ]
      


Example Output
Output 1:
 2
  Output 2:          
 0
      


Example Explanation
Explanation 1:
One of the ways to arraange them 
1. swap(5 and 6) order becomes : [3, 6, 5, 4, 1, 2]
2. swap(6 and 1) order becomes:  [3, 1, 5, 4, 6, 2]
  Explanation 2:          
No swaps required.

"""

from collections import defaultdict
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        n = A
        m = 2*n
        pair1 = defaultdict(int)
        pair2 = defaultdict(int)
       
        for i in range(n):
            pair1[C[i][0]] = C[i][1]
        
        for i in range(n):
            pair2[C[i][1]] = C[i][0]
        
        count = 0 
        i = 0
        while(i<m-1):
            if pair1[B[i]] != 0 and pair1[B[i]] != B[i+1]:
                for j in range(i+2, m):
                    if B[j] == pair1[B[i]]:
                        B[i+1], B[j] = B[j], B[i+1]
                        count += 1
            
            if pair2[B[i]] != 0 and pair2[B[i]] != B[i+1]:
                for j in range(i+2, m):
                    if B[j] == pair2[B[i]]:
                        B[i+1], B[j] = B[j], B[i+1]
                        count += 1
                        
            i += 2
        return count
