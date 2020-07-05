"""

Contact Finder
Problem Description

We want to make a custom contacts finder applications as part of our college project. The application must perform two types of operations:

Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a string in vector B denoting a contact name. This must store B[i] as a new contact in the application.

Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] is a string in vector B denoting a partial name to search the application for. It must count the number of contacts starting with B[i].

You have been given sequential add and find operations. You need to perform each operation in order.

And return as an array of integers, answers for each query of type 2(denoted by 1 in A) .



Problem Constraints
1 <= |A| <= 10000

1 <= |length of strings in B| <= 10



Input Format
First argument is the vector A, which denotes the type of query.

Second argument is the vector B, which denotes the string for corresponding query.



Output Format
Return an array of integers, denoting answers for each query of type 1.



Example Input
Input 1:

A = [0, 0, 1, 1]
B = ["hack", "hacker", "hac", "hak"]
Input 2:

A = [0, 1]
B = ["abcde", "abc"]


Example Output
Output 1:

 
[2, 0]
Output 2:

[1]


Example Explanation
Explanation 1:

 
We perform the following sequence of operations:
Add a contact named "hack".
Add a contact named "hacker".
Find the number of contact names beginning with "hac". There are currently two contact names in the application and both of them start with "hac", so we have 2.
Find the number of contact names beginning with "hak". There are currently two contact names in the application but neither of them start with "hak", so we get0.
Explanation 2:

 
Add "abcde"
Find words with prefix "abc". We have answer as 1.

"""


# Here I used a count which will tell in how many different words that letter is present.
# Insert the word in trie when A[i] = 0.
# if A[i] = 1, search that word in trie and return the value of 'count' of last letter of that word.
# If not found, return 0

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
        
    def find_partial(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return 0
            curr_node = curr_node.children[letter]
        return curr_node.count
    

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = Trie()
        n = len(A)
        ans = []
        
        for i in range(n):
            if A[i] == 0:
                trie.insert(B[i])
            else:
                ans.append(trie.find_partial(B[i]))
                
        return ans
                