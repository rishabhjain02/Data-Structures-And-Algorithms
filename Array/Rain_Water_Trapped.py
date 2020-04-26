"""

Rain Water Trapped

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 

Input Format
The only argument given is integer array A.

Output Format
Return the total water it is able to trap after raining..

For Example

Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1] 

    (For reference see the image : http://i.imgur.com/0qkUFco.png)

Output 1:
    6

Explaination 1:

    In this case, 6 units of rain water (blue section) are being trapped.

"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    n=len(A)
	    max_right=[0]*n
        max_right[n-1]=A[n-1]
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],A[i])
            
        max_left = A[0]
        water=0
        
        for i in range(len(A)):
            max_left=max(max_left,A[i])
            water += min(max_left,max_right[i])-A[i]
        
        return water
	    
