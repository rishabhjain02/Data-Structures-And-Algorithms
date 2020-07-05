"""

Shortest Unique Prefix
Problem Description

Given a list of N words. Find shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is prefix of another. In other words, the representation is always possible



Problem Constraints
1 <= Sum of length of all words <= 10^6



Input Format
First and only argument is a string array of size N.



Output Format
Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.



Example Input
Input 1:

 A = ["zebra", "dog", "duck", "dove"]
Input 2:

A = ["apple", "ball", "cat"]


Example Output
Output 1:

 ["z", "dog", "du", "dov"]
Output 2:

 ["a", "b", "c"]


Example Explanation
Explanation 1:

 Shortest unique prefix of each word is:
 For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
 For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
 For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
 For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog".  
 
Explanation 2:

 "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent.

"""



# Here I used a count which will tell in how many different words that letter is present.
# Create a trie of given words.
# Then search each word in trie, if you find any letter that has count 1, then from root to that node,
# will be our unique prefix.
# Do this for all the remaining words.

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end_of_word = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        
    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
            curr_node.count += 1
        curr_node.end_of_word = True
        
    def unique_prefix(self, word):
        l = []
        curr_node = self.root
        for letter in word:
            curr_node = curr_node.children[letter]
            l.append(curr_node.letter)
            if curr_node.count == 1:
                break
        return l
        

class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, words):
	    trie = Trie()
	    ans = []
	    
	    for word in words:
	        trie.insert(word)
	      
	    for word in words:  
	        s = "".join(trie.unique_prefix(word))
	        ans.append(s)
	        
	    return ans
	   
	    
