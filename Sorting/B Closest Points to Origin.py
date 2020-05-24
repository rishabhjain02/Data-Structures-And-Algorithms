"""

B Closest Points to Origin
Problem Description
We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0). Here, the distance between two points on a plane is the Euclidean distance. You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.) NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)^2 + (y1-y2)^2 ).     


Problem Constraints
1 <= B <= length of the list A <= 100000
-100000 <= A[i][0] <= 100000
-100000 <= A[i][1] <= 100000


Input Format
The argument given is list A and an integer B.


Output Format
Return the B closest points to the origin (0, 0) in any order.


Example Input
Input 1:
 A = [ 
       [1, 3],
       [-2, 2] 
     ]
 B = 1
Input 2:
 A = [
       [1, -1],
       [2, -1]
     ] 
 B = 1
 


Example Output
Output 1:
 [ [-2, 2] ]
Output 2:
 [ [1, -1] ]
 


Example Explanation
Explanation 1:
 The Euclidean distance will be sqrt(10) for point [1,3] and sqrt(8) for point [-2,2].
 So one closest point will be [-2,2].
Explanation 2:
 The Euclidean distance will be sqrt(2) for point [1,-1] and sqrt(5) for point [2,-1].
 So one closest point will be [1,-1].

"""

import math
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def partition(self, A, arr, low, high):
        pivot = arr[low]
        left = low+1
        right = high
        done = False
            
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
                    
            while right >= left and arr[right] >= pivot:
                right -= 1
                    
            if right < left:
                done = True
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                
                temp2 = A[left]
                A[left] = A[right]
                A[right] = temp2
    
        temp = arr[low]
        arr[low] = arr[right]
        arr[right] = temp
        
        temp2 = A[low]
        A[low] = A[right]
        A[right] = temp2
                    
        return right
    
    def quickSort(self, A, arr, low, high):
        if low < high:
            p = self.partition(A, arr, low, high)
            self.quickSort(A, arr, low, p-1)
            self.quickSort(A, arr, p+1, high)
            
    
    def solve(self, A, B):
        n = len(A)
        distance = [0]*n
        ans = [0]
        for i in range(n):
            x = A[i][0]
            y = A[i][1]
            distance[i] = math.sqrt(x*x + y*y)
        self.quickSort(A, distance, 0, n-1)
        return A[:B]




    # Second approach --->    
    # def solve(self, A, B):
    #     A.sort(key = lambda x:math.sqrt(x[0]*x[0]+x[1]*x[1]))
    #     return A[:B]
            
        
