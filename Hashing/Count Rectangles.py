"""

Count Rectangles
Problem Description

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2-D Cartesian plane.

Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.



Problem Constraints
1 <= N <= 2000
0 <= A[i], B[i] <= 10^9



Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.



Output Format
Return the number of unordered quadruplet that form a rectangle.



Example Input
Input 1:

 A = [1, 1, 2, 2]
 B = [1, 2, 1, 2]
Input 1:

 A = [1, 1, 2, 2, 3, 3]
 B = [1, 2, 1, 2, 1, 2]


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 All four given points make a rectangle. So, the answer is 1.
Explanation 2:

 3 quadruplets which make a rectangle are: (1, 1), (2, 1), (2, 2), (1, 2)
                                           (1, 1), (3, 1), (3, 2), (1, 2)
                                           (2, 1), (3, 1), (3, 2), (2, 2)


"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        points = set()
        ans = 0
        
        # Add all the points in form of tuple in points set
        for i in range(n):
            points.add((A[i], B[i]))
            
        # Now traverse each point for cur_point     
        for i in range(n):
            x1, y1 = A[i], B[i]
            
            for j in range(i+1, n):
                x2, y2 = A[j], B[j]
                
                # If both points have different x-coordinate and y-coordinate
                # Make a new point by interchanging their y-coordinate
                # If both points have either x-coordinate or y-coordinate same, the new point formed
                # will be same to those two current points
                # Hence, we do operation only if this condition satisfy.
                # It means we are taking diagonally opposite points of a rectangle and make two 
                # new points which will be two other points of rectangle and search for new points
                if (x1 != x2) and (y1 != y2):
                    new_point1 = (x1, y2)
                    new_point2 = (x2, y1)
                    
                    # If both the new points are present in set, so this is valid rectangle
                    # Hence increment the ans
                    if new_point1 in points and new_point2 in points:
                        ans += 1
        
        # For each diagonally oppsite points we are finding other two diagonally opposite points  
        # So, in this way we are counting each traingle two times (1 for each diagonally oppsite points)
        # Hence, divide by 2 to get correct no. of rectangles
        return ans//2
            
            
