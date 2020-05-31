"""

Window String
Problem Description

Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.

Note:

If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )


Problem Constraints
1 <= size(A), size(B) <= 10^6



Input Format
First argument is a string A.
Second argument is a string B.



Output Format
Return a string denoting the minimum window.



Example Input
Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"
Input 2:

 A = "Aa91b"
 B = "ab"


Example Output
Output 1:

 "BANC"
Output 2:

 "a91b"


Example Explanation
Explanation 1:

 "BANC" is a substring of A which contains all characters of B.
Explanation 2:

 "a91b" is the substring of A which contains all characters of B.

"""

from collections import defaultdict
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
	    n = len(A)
	    m = len(B)
	    start = 0
	    final_start = -1
	    min_len = float('inf')
	    count = 0
	    freq_a = defaultdict(int)
	    freq_b = defaultdict(int)
	    cur_window = 0
	    
	    # If size of B is greater than A then we can not find any substring
	    if m > n:
	        return ""
	    
	    # Storing frequency of each char of B in freq_b dict
	    for char in B:
	        freq_b[char] += 1
	        
	    # Looping through string A     
	    for i in range(n):
	        
	        # Updating the freq. of each char in A in freq_a dict
	        freq_a[A[i]] += 1
	        
	        # If the cur. char is in freq_b and freq of that char in freq_a <= that in freq_b
	        # So, that char is valid and we increase the count
	        # count is basically storing the count of char present in B and currently visited in A
	        if A[i] in freq_b and freq_a[A[i]] <= freq_b[A[i]]:
	            count += 1
	            
	        # if count == len(B) It means we have find all the required char of B
	        # Now we try to minimise our window
	        if count == m:
	            
	            # If char at start is not present in B or the freq. of that char in freq_a > freq_b
	            # It means we can move start ahead.
	            while A[start] not in freq_b or freq_a[A[start]] > freq_b[A[start]]:
	                
	                # If the freq. of char in freq_a > freq_b, So we can delete that char from freq_a
	                if freq_a[A[start]] > freq_b[A[start]]:
	                    freq_a[A[start]] -= 1
	                start += 1
	                
	            # Find current window size     
	            cur_window = i - start + 1
	            
	            # If current window in less than min_val, then update min_val and final_start
	            # Final_start will give the start index of final min possible substring
	            if cur_window < min_len:
	                min_len = cur_window
	                final_start = start
	    
	    # If final_start is -1, it means substring is not found So, return empty            
	    if final_start == -1:
	        return ""
	        
	    # Return the substring starting from final_start upto min_len
	    # Bcz min_len tell the length of min substring possible
	    return A[final_start : final_start + min_len]


