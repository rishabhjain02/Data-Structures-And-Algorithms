"""

Points inside Rectangle
Problem Description
You are given a rectangle with co-ordinates represented by arrays A and B, where the sides might not be parallel to the x-y axis. Given N points on x-y plane whose co-ordinates are represented by arrays C and D, count the number of points that lie strictly inside the rectangle. All the coordinates have integral values.    


Problem Constraints
1 <= N <= 10^2 -10^7 <= A[i], B[i], C[i], D[i] <= 10^7   


Input Format
First arguement is an interger array A of size 4 denoting the x co-ordinates of all the four corners of the rectangle. Second arguement is an interger array B of size 4 denoting the y co-ordinates of all the four corners of the rectangle. Third argument is an integer array C of size N denoting the x co-ordinates of all the N points. Fourth argument is an integer array D of size N denoting the y co-ordinates of all the N points.    


Output Format
Return an single integer denoting the count of points that lies strictly inside the rectangle.


Example Input
Input 1:
 A = [0, -2, 2, 4]
 B = [0, 2, 6, 4]
 C = [1, 2, 1, 5, -3]
 D = [3, 4, 2, 5, 1]
   


Example Output
Output 1:
 3
   


Example Explanation
Explanation 1:
 Thus, rectangle has the coordinates (0,0), (-2,2), (2,6) and (4,4).
 We see points (1, 3), (2, 4), (1, 2) lies strictly inside the rectangle whereas (5, 5), (-3, 1) lies outside the rectangle.

"""

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @param D : list of integers
	# @return an integer
	def solve(self, A, B, C, D):
	    def area(x1, y1, x2, y2, x3, y3):
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
	    
        x1, x2, x3, x4 = A[0], A[1], A[2], A[3]
        y1, y2, y3, y4 = B[0], B[1], B[2], B[3]
        	    
        def check_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
            rec_area = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x4, y4, x3, y3)
            t1_area = area(x, y, x1, y1, x2, y2)
            t2_area = area(x, y, x2, y2, x3, y3)
            t3_area = area(x, y, x3, y3, x4, y4)
            t4_area = area(x, y, x4, y4, x1, y1)
            if t1_area == 0 or t2_area == 0 or t3_area == 0 or t4_area == 0:
                return False
            return (rec_area == (t1_area + t2_area + t3_area + t4_area))
        	        
        count = 0
        n = len(C)
        for i in range(n):
            x, y = C[i], D[i]
            if check_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
                count += 1
        return count
        	   
	    
