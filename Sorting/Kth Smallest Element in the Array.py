"""

Kth Smallest Element in the Array
Problem Description
Find the Bth smallest element in given array A . NOTE: Users should try to solve it in <= B swaps. 


Problem Constraints
1 <= |A| <= 100000 1 <= B <= |A|   


Input Format
First argument is vector A. Second argument is integer B.   


Output Format
Return the Bth smallest element in given array.


Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3
  Input 2:            
A = [1, 2]
B = 2
       


Example Output
Output 1:
 2
  Output 2:            
 2
       


Example Explanation
Explanation 1:
 3rd element after sorting is 2.
  Explanation 2:            
 2nd element after sorting is 2.

"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    low = min(A)
        high = max(A)
        mid = -1
        ans = -1
        while(low <= high):
            mid = (high + low) // 2;
            count=0;
            for i in A:
                if i <= mid:
                    count += 1
            if count < B:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

