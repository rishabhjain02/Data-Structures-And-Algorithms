"""

Palindrome Partitioning
Problem Description
Given a string A, partition s such that every string of the partition is a palindrome.
 Return all possible palindrome partitioning of s. Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))
  


Problem Constraints
1 <= len(A) <= 15


Input Format
First argument is a string A of lowercase characters.


Output Format
Return a list of all possible palindrome partitioning of s.


Example Input
Input 1:
A = "aab"
   Input 2:  
A = "a"
   


Example Output
Output 1:
 [
    ["a","a","b"]
    ["aa","b"],
  ]
   Output 2:  
 [
    ["a"]
  ]
   


Example Explanation
Explanation 1:
In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").
   Explanation 2:  
In the given example, only partition possible is "a" .

"""

from collections import defaultdict
class Solution:
    # @param A : string
    # @return a list of list of strings
    
    def getPalindromeMap(self, s):
        palindrome_map = defaultdict(int)
        n = len(s)
        for i in range(n):
            for j in range(n):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    palindrome_map[temp] = 1
        return palindrome_map
        
    def find_partition(self, s, cur_idx, cur_str, ans, n, palindrome_map):
        if cur_idx == n:
            ans.append(cur_str[:])
            return
        
        for j in range(cur_idx, n):
            temp = s[cur_idx:j+1]
            if palindrome_map[temp]:
                cur_str.append(temp)
                self.find_partition(s, j+1, cur_str, ans, n, palindrome_map)
                cur_str.pop()
                
    
    def partition(self, A):
        n = len(A)
        ans = []
        cur_str = []
        palindrome_map = self.getPalindromeMap(A)
        self.find_partition(A, 0, cur_str, ans, n, palindrome_map)
        return ans
        
        
