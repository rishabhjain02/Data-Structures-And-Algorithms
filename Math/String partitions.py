"""

String partitions
Problem Description
Given an integer A denoting length of a string, find the number of ways of breaking the string it into 3 strings of length x,y,z such that:
x >= B
y >= C
z >= D
 Return the number of ways. Since the answer can get huge, return answer modulo 10^9 + 7 Note that your solution will be run against more than 10,000 test cases.    


Problem Constraints
1 <= A <= 10^9 0 <= B + C + D <= A 0 <= B, C, D <= 10^9    


Input Format
First argument is an integer A.
Second argument is an integer B.
Third argument is an integer C.
Fourth argument is an integer D.


Output Format
Return the number of ways of breaking the string into 3 strings of length x,y,z such that all the 3 stated conditions are true. Since the answer can get huge, return answer modulo 10^9 + 7.


Example Input
Input 1:
 A = 4
 B = 0 
 C = 1
 D = 0
 Input 2:
 A = 4
 B = 3 
 C = 1
 D = 0
 


Example Output
Output 1:
 10
Output 2:
 1
   


Example Explanation
Explanation 1:
 All the 10 possible values are: (0,1,3),(0,2,2),(0,3,1),(0,4,0),(1,1,2),(1,2,1),(1,3,0),(2,1,1),(2,2,0),(3,1,0).
Explanation 2:
 Only one posible answer: (3,1,0)

"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        # we have to find only (A-B-C-D+2)C2
        return ((A-B-C-D+2)*(A-B-C-D+1)//2) % 1000000007


