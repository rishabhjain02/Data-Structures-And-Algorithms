"""

Maximum Frequency stack
Problem Description

You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.

Operations are of two types:

1 x: push an integer x onto the stack and return -1

2 0: remove and return the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.



Problem Constraints
1 <= N <= 100000

1 <= A[i][0] <= 2

0 <= A[i][1] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the array of integers denoting answer to each operation.



Example Input
Input 1:

A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Input 2:

 A =  [   
        [1, 5]
        [2 0]
        [1 4]   ]


Example Output
Output 1:

 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]
Output 2:

 [-1, 5, -1]


Example Explanation
Explanation 1:

 Just simulate given operations
Explanation 2:

 Just simulate given operations

"""

from collections import defaultdict
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        max_freq = 0
        freq = defaultdict(int)
        freq_stack = defaultdict(list)
        ans = []
        
        for val in A:
            oper = val[0]
            x = val[1]
            
            if oper == 1:
                freq[x] += 1
                freq_stack[freq[x]].append(x)
                max_freq = max(max_freq, freq[x])
                ans.append(-1)
                
            else:
                temp = freq_stack[max_freq].pop()
                freq[temp] -= 1
                if freq_stack[max_freq] == []:
                    max_freq -= 1
                ans.append(temp)
        
        return ans