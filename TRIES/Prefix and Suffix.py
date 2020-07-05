"""

Prefix and Suffix
Problem Description

Given a list of N words denoted by string array A of size N.

You have to answer Q queries denoted by string array B, for each query you have a string S of size M, find the number of words in the list A which have string S as a prefix and suffix.

NOTE: The size M for all strings in the queries remains same.



Problem Constraints
1 <= N <= 10^5

1 <= |A[i]| <= 1000

1 <= Q, M <= 1000

Sum of length of all N words <= 10^6



Input Format
First argument is a string array A of size N denoting the list of words.

Second argument is a string array B of size Q denoting the queries.



Output Format
Return an integer array of size Q denoting the answer of each query.



Example Input
Input 1:

 A = ["ababa", "aabbvaab", "aecdsaaec", "abaaxbqaba"]
 B = ["aba", "aec", "abb", "aab"]
Input 2:

 A = ["cazqzqcaz", "cadssac", "caz"]
 B = ["caz", "cad"]


Example Output
Output 1:

 [2, 1, 0, 1]
Output 2:

 [2, 0]


Example Explanation
Explanation 1:

 2 word "ababa" and "abaaxbqaba" has both prefix and suffix "aba".
 1 word "aecdsaaec" has both prefix and suffix "aec".
 No word has both prefix and suffix "abb".
 1 word "aabbvaab" has both prefix and suffix "aab".
Explanation 2:

 2 word "cazqzqcaz" and "caz" has both prefix and suffix "caz".
 No word has both prefix and suffix "cad".

"""


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end_of_word = False
        self.frequency = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        
    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.end_of_word = True
        curr_node.frequency += 1
        
    def word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False, 0
            curr_node = curr_node.children[letter]
        return curr_node.end_of_word, curr_node.frequency

def valid_word(word, count):
    n = len(word)
    if n < count:
        return False
    
    start = 0
    end = n-count
    for i in range(count):
        if word[start] != word[end]:
            return False
        start += 1
        end += 1
    
    return True

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        count = len(B[0])
        ans = []
        
        trie = Trie()
        
        for word in A:
            if valid_word(word, count):
                trie.insert(word[:count])
                
        for word in B:
            exist, freq = trie.word_exist(word)
            ans.append(freq)
                
        return ans
                
        
        
