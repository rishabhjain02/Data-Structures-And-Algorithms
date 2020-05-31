"""

Anagrams
Problem Description

Given an array A of N strings, return all groups of strings that are anagrams.

Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.

NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'.



Problem Constraints
1 <= N <= 10^4

1 <= |A[i]| <= 10^4

Each string consists only of lowercase characters.

Sum of length of all the strings doesn't exceed 10^7



Input Format
Single Argument A which is an array of strings.



Output Format
Return a two-dimensional array where each row describes a group.

Note:

Ordering of the result :
You should not change the relative ordering of the strings within the group suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.



Example Input
Input 1:

 A = [cat, dog, god, tca]
Input 2:

 A = [rat, tar, art]


Example Output
Output 1:

 [ [1, 4],
   [2, 3] ]
Output 2:

 [ [1, 2, 3] ]


Example Explanation
Explanation 1:

 "cat" and "tca" are anagrams which correspond to index 1 and 4 and "dog" and "god" are another set of anagrams which correspond to index 2 and 3.
 The indices are 1 based ( the first element has index 1 instead of index 0).
Explanation 2:

 All three strings are anagrams.

"""

from collections import defaultdict
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
	    n = len(A)
	    ans = defaultdict(list)
        
        for i in range(n):
            count = [0] * 26
            
            # fill the count list with freq of each character in A[i]
            # a is at 0th index, b at 1 index and so on....
            for c in A[i]:
                count[ord(c) - ord('a')] += 1
                
            # ans - <tuple> : <list>
            # This ans map will store count list in form of tuple as the key and
            # list of index(1 based indexing) of the strings as the value
            # So, in this way every anagram string will have same count tuple
            # and we just append the index of that string
            ans[tuple(count)].append(i+1)
        
        return list(ans.values())
	    