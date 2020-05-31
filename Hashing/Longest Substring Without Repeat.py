"""

Longest Substring Without Repeat
Problem Description

Given a string A, find the length of the longest substring without repeating characters.



Problem Constraints
1 <= size(A) <= 10^6

String consists of lowerCase,upperCase characters and digits are also present in the string A.



Input Format
Single Argument representing string A.



Output Format
Return an integer denoting the maximum possible length of substring without repeating characters.



Example Input
Input 1:

 A = "abcabcbb"
Input 2:

 A = "AaaA"


Example Output
Output 1:

 3
Output 2:

 2


Example Explanation
Explanation 1:

 Substring "abc" is the longest substring without repeating characters in string A.
Explanation 2:

 Substring "Aa" or "aA" is the longest substring without repeating characters in string A.


"""

from collections import defaultdict
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
	    freq = defaultdict(int)
	    n = len(A)
	    if n == 1:
	        return 1
	    start = 0
	    end = 0
	    ans = 0
	    
	    while(end < n):
	        if not freq[A[end]]:
	            freq[A[end]] = 1
	            end += 1
	        else:
	            ans = max(ans, end - start)
	            while freq[A[end]] > 0:
	                freq[A[start]] = 0
	                start += 1
	                
	    ans = max(ans, end-start)
	    return ans
