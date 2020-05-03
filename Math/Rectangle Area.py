"""

Rectangle Area
Problem Description
Given eight integers A, B, C, D, E, F, G and H which represent two rectangles in a 2D plane. For the first rectangle it's bottom left corner is (A, B) and top right corner is (C, D) and for the second rectangle it's bottom left corner is (E, F) and top right corner is (G, H). Find and return the overlapping area of the two rectangles. 


Problem Constraints
-10^4 <= A <= C <= 10^4
-10^4 <= B <= D <= 10^4
-10^4 <= E <= G <= 10^4
-10^4 <= F <= H <= 10^4


Input Format
The eight arguments given are the integers A, B, C, D, E, F, G and H.


Output Format
Return the overlapping area of the two rectangles.


Example Input
Input 1:
 A = 0   B = 0
 C = 4   D = 4
 E = 2   F = 2
 G = 6   H = 6
Input 2:
 A = 0   B = 0
 C = 4   D = 4
 E = 2   F = 2
 G = 3   H = 3


Example Output
Output 1:
 4
Output 2:
 1

"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
        
        left1, right1, bottom1, top1 = A, C, B, D
        left2, right2, bottom2, top2 = E, G, F, H
        
        x_value = max(0, min(right1,right2) - max(left1,left2))
        y_value = max(0, min(top1,top2) - max(bottom1,bottom2))
        
        return x_value*y_value
        
        
