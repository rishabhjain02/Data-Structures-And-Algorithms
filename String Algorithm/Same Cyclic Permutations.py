"""

Same Cyclic Permutations
Given two String A, B of same length.

Find the number of cyclic permutations of B that are same as A.

Input Format

Given two arguments A, B of type String.
Output Format

Return a single integer N, i.e number of Cyclic Permuations of B same as A.
Constraints

1 <= length(A) = length(B) <= 1e5
Example

Example Input :
    A = aba
    B = aba

Example Output :
    1

Explanation :
    All cyclic permutations of B are :
    1. aba
    2. baa
    3. aab
    here cyclic permutations 1 is same as A so ans is 1.

"""

def find_Z_array(s, z):
    n = len(s)
    l = 0
    r = 0
    for k in range(1, n):
        if k > r:
            l = k
            r = k
            
            while r<n and s[r-l] == s[r]:
                r += 1
            z[k] = r-l
            r -= 1
        
        else:
            j = k - l
            
            if z[j] < r - k + 1:
                z[k] = z[j]
                
            else:
                l = k
                while r<n and s[r-l] == s[r]:
                    r += 1
                z[k] = r-l
                r -= 1 

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        s = A+"$"+B+B
        n = len(s)
        z = [0]*n
        find_Z_array(s, z)
        
        count = 0
        for i in range(n):
            if z[i] == len(A):
                count += 1
        return count-1
        
        
        
