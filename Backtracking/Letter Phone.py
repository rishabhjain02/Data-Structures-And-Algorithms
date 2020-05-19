"""

Letter Phone
Given a digit string, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below.  The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.

Image : http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.

"""

class Solution:
	# @param A : string
	# @return a list of strings
	def findAns(self, string, cur_idx, n, buttons_map, ans, temp):
	    
	    if cur_idx == n:
	        ans.append(temp)
	        return 
	    
	    s = buttons_map[string[cur_idx]]
	    
	    for i in range(len(s)):
	        temp += s[i]
	        self.findAns(string, cur_idx+1, n, buttons_map, ans, temp)
	        temp = temp[:-1]
	    
	def letterCombinations(self, A):
	    buttons_map = {"0":"0", "1":"1", "2":"abc", 
	                    "3":"def", "4":"ghi", "5":"jkl", 
	                    "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
	    ans = []
	    n = len(A)
	    temp=""
	    self.findAns(A, 0, n, buttons_map, ans, temp)
	    return ans
