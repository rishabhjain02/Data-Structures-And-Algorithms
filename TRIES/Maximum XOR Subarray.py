"""

Maximum XOR Subarray
Problem Description

Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N which has maximum XOR value.

NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length. If length is same, return the subarray with minimum starting index.



Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 10^9



Input Format
First and only argument is an integer array A.



Output Format
Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray and B[1] is the ending index(1-based) of the subarray.



Example Input
Input 1:

 A = [1, 4, 3]
Input 2:

 A = [8]


Example Output
Output 1:

 [2, 3]
Output 2:

 [1, 1]


Example Explanation
Explanation 1:

 There are 6 possible subarrays of A:
 subarray            XOR value
 [1]                     1
 [4]                     4
 [3]                     3
 [1, 4]                  5 (1^4)
 [4, 3]                  7 (4^3)
 [1, 4, 3]               6 (1^4^3)

 [4, 3] subarray has maximum XOR value. So, return [2, 3].
Explanation 2:

 There is only one element in the array. So, the maximum XOR value is equal to 8 and the only possible subarray is [1, 1].

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
    A = list(set(A))
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
    
# Function to convert array of bits to decimal number    
def decimal(arr):
    ans = 0
    n = len(arr)
    for i in range(n-1, -1, -1):
        ans += (2**(n-i-1))*arr[i]
        
    return ans

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        start_index = 0
        end_index = 0
        trie = Trie()
        if n == 1:
            return [1, 1]
            
        prefix_xor = [0]*(n+1)
        indices = defaultdict(int)
        
        for i in range(1, n+1):
            prefix_xor[i] = prefix_xor[i-1] ^ A[i-1]
        
        for i in range(n+1):
            if prefix_xor[i] not in indices:
                indices[prefix_xor[i]] = i
        
        # prefix_xor = list(set(prefix_xor))
        # print(prefix_xor)
        
        binary = defaultdict(list)
        
        # Fill the binary hashmap 
        make_binary(prefix_xor, binary)
        
        # Insert each num in trie in binary form
        for num in prefix_xor:
            trie.insert(binary[num])
            
        ans = 0    
        for i in range(len(prefix_xor)):
            temp = []
            
            # Finding max XOR bits
            trie.best_xor_value(binary[prefix_xor[i]], temp)
            
            # Finding max possible XOR from all
            xor = find_xor(binary[prefix_xor[i]], temp)
            if ans < xor:
                ans = xor
                start_index = min(indices[prefix_xor[i]], indices[decimal(temp)])
                end_index = max(indices[prefix_xor[i]], indices[decimal(temp)])
                
            # If new xor is same as ans, so we will check length of subarray
            # if new length is small then, update the start and end index
            if ans == xor:
                val1 = min(indices[prefix_xor[i]], indices[decimal(temp)])
                val2 = max(indices[prefix_xor[i]], indices[decimal(temp)])
                if val2-val1 < end_index-start_index:
                    start_index = val1
                    end_index = val2
        
        # if our final ans(max xor) is present in array itself as an element
        # then that will be the subarray of smallest length
        for i in range(n):
            if A[i] == ans:
                return [i+1, i+1]
        
        return [start_index+1, end_index]
        
        