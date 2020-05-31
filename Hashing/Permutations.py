"""

Permutations
Problem Description

You are given two strings A and B of size N and M respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints
1 <= N < M <= 10^5



Input Format
Given two argument, A and B of type String.



Output Format
Return a single Integer, i.e number of permutations of A present in B as a substring.



Example Input
Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output
Output 1:

 5
Output 2:

 2


Example Explanation
Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa 

"""

# Function to check two freq array are equal or not
def equal(hash_a, hash_b):
    for i in range(26):
        if hash_a != hash_b:
            return False
    return True

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        hash_a = [0]*26
        hash_b = [0]*26
        ans = 0
        
        # count frequency of each char in A
        for i in range(n):
            hash_a[ord(A[i]) - ord('a')] += 1
         
        # count frequency of each char in B for first window of size n    
        for i in range(n):
            hash_b[ord(B[i]) - ord('a')] += 1
        
        # Checking for first window
        if equal(hash_a, hash_b):
            ans += 1
            
        start = 0    
        
        # Sliding the window by one place and decreasing the count of leftmost char each time 
        # and increasing the count of current char each time and checking for equal(hash_a, hash_b)
        for i in range(n, m):
            hash_b[ord(B[start]) - ord('a')] -= 1
            hash_b[ord(B[i]) - ord('a')] += 1
            if equal(hash_a, hash_b):
                ans += 1
            start += 1
        
        return ans
