"""

Divide Integers
Problem Description
Divide two integers without using multiplication, division and mod operator. Return the floor of the result of the division. Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX. NOTE: INT_MAX = 2^31 - 1  


Problem Constraints
-2^31 <= A, B <= 2^31-1 B!= 0  


Input Format
First argument is an integer A denoting the dividend.
Second argument is an integer B denoting the divisor.


Output Format
Return an integer denoting the floor value of the division.


Example Input
Input 1:
 A = 5
 B = 2
Input 2:
 A = 7
 B = 1
  


Example Output
Output 1:
 2
Output 2:
 7
  


Example Explanation
Explanation 1:
 floor(5/2) = 2

"""

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def divide(self, A, B):
	    
	   #################################################################################
	   
	   # Approach 1: Refer notes
	    
	    intMax = 2147483647
	    intMin = -2147483648
	    
	    if A<intMin or A>intMax:
	        return intMax
	        
	    elif A == 0:
	        return 0
	        
        s = 0
        ans = 0
        count = int(math.log2(abs(A)))
        for i in range(count,-1,-1):
            if (s + (abs(B)<<i)) <= abs(A):
                s += abs(B)<<i
                ans += 2**i
        
	        
	    if A == intMin and B == -1:
	        return intMax
	        
	    elif A == intMin and B == 1:
	        return intMin
	        
	    elif (A == intMax and B == -1) or (A == intMax and B == 1):
	        return intMax*B
	        
	    elif (A<0 and B<0) or (A>0 and B>0):
	        return ans
	        
	    else:
	        return -1 * ans
                
	   
	   
	   
	   
	   #################################################################################
	   
	   # Approach 2:
	   
	   # intMax = 2147483647
	   # intMin = -2147483648
	    
	   # if A<intMin or A>intMax:
	   #     return intMax
	        
	   # elif A == 0:
	   #     return 0
	        
	   # elif A == intMin and B == -1:
	   #     return intMax
	        
	   # elif A == intMin and B == 1:
	   #     return intMin
	        
	   # elif (A == intMax and B == -1) or (A == intMax and B == 1):
	   #     return intMax*B
	        
	   # elif (A<0 and B<0) or (A>0 and B>0):
	   #     return int(2**(math.log2(abs(A)) - math.log2(abs(B))))
	        
	   # else:
	   #     return -1 * int(2**(math.log2(abs(A)) - math.log2(abs(B))))
	   
	   
	        
