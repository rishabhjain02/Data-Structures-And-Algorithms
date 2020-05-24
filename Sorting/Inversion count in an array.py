"""

Inversion count in an array
Problem Description
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (10^9 + 7).


Problem Constraints
1 <= length of the array <= 100000 1 <= A[i] <= 10^9   


Input Format
The only argument given is the integer array A.


Output Format
Return the number of inversions of A modulo (10^9 + 7).


Example Input
Input 1:
A = [3, 2, 1]
  Input 2:            
A = [1, 2, 3]
       


Example Output
Output 1:
3
  Output 2:            
0
       


Example Explanation
Explanation 1:
 All pairs are inversions.
  Explanation 2:            
 No inversions.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    
    def merge_sort(self, arr, ans):
        if len(arr) > 1:
    		mid = len(arr) // 2
    		left_array = arr[:mid]
    		right_array = arr[mid:]
    
    		self.merge_sort(left_array, ans)
    		self.merge_sort(right_array, ans)
    		
    		i = 0
            j = 0
            k = 0
                        
            while i<len(left_array) and j<len(right_array):
    			if left_array[i] <= right_array[j]:
    				arr[k] = left_array[i]
    				i += 1
    			else:
    			    # here we are updating the ans as if left_array[i] > right_array[j] : all the 
    			    # elements from i to len(left_array[i]) will be greater than right_array[j].
    			    # Hence, append all the elements.
    			    
    			    ans[0] = (ans[0] + (len(left_array) - i))%(10**9+7)
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
