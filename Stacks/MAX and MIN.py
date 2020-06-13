"""

MAX and MIN
Problem Description

Given an array of integers A .

value of a array = max(array) - min(array).

Calculate and return the sum of values of all possible subarrays of A % 10^9+7.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 1000000



Input Format
The first and only argument given is the integer array A.



Output Format
Return the sum of values of all possible subarrays of A % 10^9+7.



Example Input
Input 1:

 A = [1]
Input 2:

 A = [4, 7, 3, 8]


Example Output
Output 1:

 0
Output 2:

 26


Example Explanation
Explanation 1:

Only 1 subarray exists. Its value is 0.
Explanation 2:

value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26

"""

# Function to find the index of just smaller element in left side for all the elements.
def find_left_smaller(A, left_smaller):
    n = len(A)
    stack = [0]
        
    for i in range(1,n):
        if stack != [] and A[stack[-1]] < A[i]:
	        left_smaller[i] = stack[-1]
	        stack.append(i)
	            
	    else:
	        while stack != [] and A[stack[-1]] > A[i]:
	            stack.pop()
	        if stack != []:
	            left_smaller[i] = stack[-1]
	        stack.append(i)
	        
	        
# Function to find the index of just smaller element in right side for all the elements.
def find_right_smaller(A, right_smaller):
    n = len(A)
    stack = [n-1]
    
    for i in range(n-2, -1, -1):
        if stack != [] and A[stack[-1]] < A[i]:
            right_smaller[i] = stack[-1]
	        stack.append(i)
	            
	    else:
	        while stack != [] and A[stack[-1]] > A[i]:
	            stack.pop()
	        if stack != []:
	            right_smaller[i] = stack[-1]
	        stack.append(i)
	       
	        
# Function to find the index of just greater element in left side for all the elements.	        
def find_left_greater(A, left_greater):
    n = len(A)
    stack = [0]
    
    for i in range(1, n):
        if stack != [] and A[stack[-1]] > A[i]:
            left_greater[i] = stack[-1]
            stack.append(i)
            
        else:
            while(stack != [] and A[stack[-1]] < A[i]):
                stack.pop()   
            if stack != []:
                left_greater[i] = stack[-1]
            stack.append(i)
            
            
# Function to find the index of just greater element in right side for all the elements.            
def find_right_greater(A, right_greater):
    n = len(A)
    stack = [n-1]
    
    for i in range(n-2, -1, -1):
        if stack != [] and A[stack[-1]] > A[i]:
            right_greater[i] = stack[-1]
            stack.append(i)
            
        else:
            while(stack != [] and A[stack[-1]] < A[i]):
                stack.pop()
            if stack != []:
                right_greater[i] = stack[-1]
            stack.append(i)
    

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        # For storing the index of just smaller no. in left side
        left_smaller = [-1]*n
        
        # For storing the index of just smaller no. in right side
        right_smaller = [n]*n
        
        # For storing the index of just greater no. in left side
        left_greater = [-1]*n
        
        # For storing the index of just greater no. in right side
        right_greater = [n]*n
        
        
        # For storing the count of smaller numbers in left side
        count_left_smaller = [0]*n
        
        # For storing the count of smaller numbers in right side
        count_right_smaller = [0]*n
        
        # For storing the count of greater numbers in left side
        count_left_greater = [0]*n
        
        # For storing the count of greater numbers in right side
        count_right_greater = [0]*n
        
        # For storing the contribution of any element as the max element in the subarray
        # Basically, it will give the no. of subarrays in which element i appears as max element 
        contribution_max = [0]*n
        
        # For storing the contribution of any element as the min element in the subarray
        # Basically, it will give the no. of subarrays in which element i appears as min element
        contribution_min = [0]*n
        
        ans = 0
        mod = 10**9+7
        
        find_left_smaller(A, left_smaller)
	    find_right_smaller(A, right_smaller)        
	     
	    find_left_greater(A, left_greater)
	    find_right_greater(A, right_greater)
        
        
        # Counting left greater and left smaller elements for each element
        for i in range(1, n):
            count_left_greater[i] = i - left_smaller[i] - 1
            count_left_smaller[i] = i - left_greater[i] - 1
            
            
        # Counting right greater and right smaller elements for each element
        for i in range(n-2, -1, -1):
            count_right_greater[i] = right_smaller[i] - i - 1
            count_right_smaller[i] = right_greater[i] - i - 1
            
        
        # Finding contribution: Formula = (x+1)*(y+1)
        # For contribution as max: x is count of left smaller and y is count of right smaller
        # For contribution as min: x is count of left greater and y is count of right greater
        for i in range(n):
            contribution_max[i] = ((count_left_smaller[i] + 1)%mod * (count_right_smaller[i] + 1)%mod)%mod
            contribution_min[i] = ((count_left_greater[i] + 1)%mod * (count_right_greater[i] + 1)%mod)%mod
        
        # Finding ans = (contribution as max - contribution as min)*cur_element
        for i in range(n):
            ans = (ans + ((contribution_max[i] - contribution_min[i]) * A[i])%mod)%mod
            
        return ans
