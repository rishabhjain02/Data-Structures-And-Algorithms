"""

Maximum XOR
Problem Description

Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.



Problem Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return an integer denoting the maximum result of A[i] XOR A[j].



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 7
Output 2:

 117


Example Explanation
Explanation 1:

 Maximum XOR occurs between element of indicies(0-based) 1 and 4 i.e. 2 ^ 5 = 7.
Explanation 2:

 Maximum XOR occurs between element of indicies(0-based) 1 and 2 i.e. 17 ^ 100 = 117.

"""


import math
from collections import defaultdict

# Trie node class
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
   
# Trie class        
class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        
    # Function for inserting array of bits(binary representation of a no.) to trie
    # 0 will be left child and 1 will be right child
    def insert(self, arr):
        node = self.root
        for n in arr:
            if n == 1:
                if node.right == None:
                    node.right = TrieNode(1)
                node = node.right
            else:
                if node.left == None:
                    node.left = TrieNode(0)
                node = node.left
        
    # Function which traverse the tree and give best possible sequence of bits(temp) for a
    # given arr(binary representation of a number).
    # temp will be the best sequence of possible bits which will give max XOR with arr
    def best_xor_value(self, arr, temp):
        node = self.root
        
        for n in arr:
            if n == 0 and node.right != None:
                node = node.right
                temp.append(node.val)
            
            elif n == 1 and node.left != None:
                node = node.left
                temp.append(node.val)
                
            else:
                if node.left != None:
                    node = node.left
                    temp.append(node.val)
                else:
                    node = node.right
                    temp.append(node.val)
        
# Function to make a hashmap of all numbers of array with key as the numbers and value as the binary 
# representation of each number
def make_binary(A, binary):
    n = len(A)
    bits = int(math.log2(max(A))+1)
    
    for i in range(bits-1, -1, -1):
        for num in A:
            if num & (1<<i) != 0:
                binary[num].append(1)
            else:
                binary[num].append(0)
                
# Function to find XOR value in decimal from the given two arrays which contain binary representations
# of two numbers.
def find_xor(arr1, arr2):
    n = len(arr1)
    val = 0
    for i in range(n-1, -1, -1):
        val += ((2**(n-i-1))*(arr1[i]^arr2[i]))
    
    return val
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        trie = Trie()
        A = list(set(A))
        
        if max(A) == 0:
            return 0
        
        binary = defaultdict(list)
        
        # Fill the binary hashmap 
        make_binary(A, binary)
        
        # Insert each num in trie in binary form
        for num in A:
            trie.insert(binary[num])
            
        ans = 0    
        for num in A:
            temp = []
            
            # Finding max XOR bits
            trie.best_xor_value(binary[num], temp)
            
            # Finding max possible XOR from all
            ans = max(ans, find_xor(binary[num], temp))
        
        return ans
        
        
        
