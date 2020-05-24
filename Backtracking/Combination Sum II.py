"""

Combination Sum II
Problem Description
Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.  Each number in A may only be used once in the combination. Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
 Warning: DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS. Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.     


Problem Constraints
1 <= N <= 20


Input Format
First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number.


Output Format
Return all unique combinations in A where the candidate numbers sums to B.


Example Input
Input 1:
 A = [10, 1, 2, 7, 6, 1, 5]
 B = 8
Input 2:
 A = [2, 1, 3]
 B = 3


Example Output
Output 1:
 [ 
  [1, 1, 6 ],
  [1, 2, 5 ],
  [1, 7 ], 
  [2, 6 ] 
 ]
Output 2:
 [
  [1, 2 ],
  [3 ]
 ]
   


Example Explanation
Explanation 1:
 1 + 1 + 6 = 8
 1 + 2 + 5 = 8
 1 + 7 = 8
 2 + 6 = 8
 All the above combinations sum to 8 and are arranged in ascending order.
Explanation 2:
 1 + 2 = 3
 3 = 3
 All the above combinations sum to 3 and are arranged in ascending order.

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def find_combinationSum(self, A, s, cur_idx, n, cur_set, ans, items):

        if s == 0:
            temp = cur_set[:]
            temp2 = tuple(temp)
            if temp2 not in items:
                ans.append(temp)
                items.add(temp2)
            return
        
        if cur_idx == n or s < 0:
            return 
        
        # Including the current element
        cur_set.append(A[cur_idx])
        self.find_combinationSum(A, s-A[cur_idx], cur_idx+1, n, cur_set, ans, items)
        cur_set.pop()
        
        # Not including the current element
        self.find_combinationSum(A, s, cur_idx+1, n, cur_set, ans, items)
    
    def combinationSum(self, A, B):
        A.sort()
        cur_set = []
        ans = []
        n = len(A)
        items = set()
        self.find_combinationSum(A, B, 0, n, cur_set, ans, items)
        return ans
        
