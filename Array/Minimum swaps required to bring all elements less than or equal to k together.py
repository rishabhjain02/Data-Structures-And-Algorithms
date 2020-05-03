"""

Minimum swaps required to bring all elements less than or equal to k together
Problem Description
Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together. Note: It is possible to swap any two elements, not necessarily consecutive. 


Problem Constraints
1 <= length of the array <= 100000
-10^9 <= A[i], B <= 10^9


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the minimum number of swaps.


Example Input
Input 1:
A = [1, 12, 10, 3, 14, 10, 5]
B = 8
Input 2:
A = [5, 17, 100, 11]
B = 20


Example Output
Output 1:
2
Output 2:
1


Example Explanation
Explanation 1:
A = [1, 12, 10, 3, 14, 10, 5]
After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
Now, all elements less than or equal to 8 are together.

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        n = len(A)
        window = 0  # window is the total numbers in list less than or equal to B
        for i in range(n):
            if A[i] <= B:
                window += 1
        
        if window == n:
            return 0
            
        unwanted = 0
        # calculating unwanted or numbers greater than B in starting window
        for i in range(window):
            if A[i] > B:
                unwanted += 1
                
        i = 0
        j = window
        swaps = unwanted
        while i<n and j<n:
            if A[i] > B:
                unwanted -= 1
                
            if A[j] > B:
                unwanted += 1
                
            swaps = min(swaps, unwanted)
            
            i += 1
            j += 1
            
        
        return swaps
                