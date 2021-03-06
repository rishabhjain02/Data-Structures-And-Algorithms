"""

Largest Number
Problem Description
Given a array A of non negative integers, arrange them such that they form the largest number. Note: The result may be very large, so you need to return a string instead of an integer.   


Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*10^9


Input Format
First argument is an array of integers.


Output Format
Return a string representing the largest number.


Example Input
Input 1:
 A = [3, 30, 34, 5, 9]
Input 2:
 A = [2, 3, 9, 0]
  


Example Output
Output 1:
 "9534330"
Output 2:
 "9320"
 


Example Explanation
Explanation 1:
 A = [3, 30, 34, 5, 9]
 Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:
 Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320. 

"""

def myComparator(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    return ((int(yx) > int(xy)) - (int(yx) < int(xy))) 
    
def compare(mycmp):
    
    class C(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
            
    return C

class Solution:
    # @param A : tuple of integers
    # @return a strings
    
    def largestNumber(self, A):
        if max(A) == 0:
            return 0
        sorted_arr = sorted(A, key = compare(myComparator))
        ans = "".join([str(i) for i in sorted_arr])
        return ans



# Second approach ---->

# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
#         new_val = []
#         ans = ""
#         max_len = len(str(max(A))) + 1
        
#         if max(A) == 0:
#             return 0
            
#         for num in A:
#             temp = str(num)*max_len
#             new_val.append((temp[:max_len], num))
            
#         new_val.sort(reverse = True)
        
#         for i in new_val:
#             ans += str(i[1])
            
#         return ans
