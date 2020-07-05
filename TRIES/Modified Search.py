"""

Modified Search
Problem Description

Given two arrays of strings A of size N and B of size M.

Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly one modification in B[i], Else C[i] = '0'.

NOTE: modification is defined as converting a character into another character.



Problem Constraints
1 <= N <= 30000

1 <= M <= 2500

1 <= length of any string either in A or B <= 20

strings contains only lowercase alphabets



Input Format
First argument is the string arrray A.

Second argument is the string array B.



Output Format
Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using one modification in B[i], Else C[i] = '0'.



Example Input
Input 1:

 A = [data, circle, cricket]
 B = [date, circel, crikket, data, circl]
Input 2:

 A = [hello, world]
 B = [hella, pello, pella]


Example Output
Output 1:

 "10100"
Output 2:

 "110"


Example Explanation
Explanation 1:

 1. date = dat*(can be found in A)
 2. circel =(cannot be found in A using exactly one modification)
 3. crikket = cri*ket(can be found in A)
 4. data = (cannot be found in A using exactly one modification)
 5. circl = (cannot be found in A using exactly one modification)
Explanation 2:

 Only pella cannot be found in A using only one modification.

"""


# Here I am generating all the almost similar words for each word in query by changing one character at
# a time. Now I search for all the generated words in the trie, if I found any word, ans = 1 else ans = 0

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end_of_word = False
        
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
        
    def word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.end_of_word

# Function for generating all the almost matching words
def almost_matching_words(word):
    l = []
    s = "abcdefghijklmnopqrstuvwxyz"
    n = len(word)
    for i in range(n):
        for char in s:
            if word[i] != char:
                l.append(word[:i]+char+word[i+1:])
    return l 

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, dictionary, query):
        n = len(dictionary)
        m = len(query)
        trie = Trie()
        ans = []
        
        for word in dictionary:
            trie.insert(word)
        
        for word in query:
            l = almost_matching_words(word)
            flag = False
            for matching_word in l:
                if trie.word_exist(matching_word):
                    ans.append("1")
                    flag = True
                    break
            
            if flag == False:
                ans.append("0")
        
        return "".join(ans)
        
        
