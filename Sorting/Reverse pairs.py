"""

Reverse pairs
Problem Description
Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j]. Return the number of important reverse pairs in the given array A. 


Problem Constraints
1 <= length of the array <= 100000 1 <= A[i] <= 10^9  


Input Format
The only argument given is the integer array A.


Output Format
Return the number of important reverse pairs in the given array A.


Example Input
Input 1:
 A = [1, 3, 2, 3, 1]
Input 2:
 A = [4, 1, 2]


Example Output
Output 1:
 2
Output 2:
 1


Example Explanation
Explanation 1:
 There are two pairs which are important reverse i.e (3, 1) and (3, 1).
Explanation 2:
 There is only one pair i.e (4, 1).

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    		
    # Function to check how many combinations possible for left_array[i] > 2*right_array[j] and update ans
    def find_ans(self, left_array, right_array, ans):
        n = len(left_array)
        m = len(right_array)
        i = 0
        j = 0
        while(i < n and j < m):
            if left_array[i] <= 2*right_array[j]:
                i += 1
            else:
                ans[0] += n - i
                j += 1
    
    def merge_sort(self, arr, ans):
        if len(arr) > 1:
    		mid = len(arr) // 2
    		left_array = arr[:mid]
    		right_array = arr[mid:]
    
    		self.merge_sort(left_array, ans)
    		self.merge_sort(right_array, ans)
            
            # Each time we are getting sorted left_array and right_array, we are finding reverse pairs
            self.find_ans(left_array, right_array, ans)
                		
    		i = 0
            j = 0
            k = 0
        
            while i<len(left_array) and j<len(right_array):
    			if left_array[i] <= right_array[j]:
    				arr[k] = left_array[i]
    				i += 1
    			else:
    				arr[k] = right_array[j]
    				j += 1
    			k+=1
    
    		# Adding remaining elements of left array
    
    		while i<len(left_array):
    			arr[k] = left_array[i]
    			i += 1
    			k += 1
    
    
    		# Adding remaining elements of right array
    
    		while j<len(right_array):
    			arr[k] = right_array[j]
    			j += 1
    			k += 1
    		
    		
    
    def solve(self, A):
        ans = [0]
        self.merge_sort(A, ans)
        return ans[0]
