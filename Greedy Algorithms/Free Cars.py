"""

Free Cars
Problem Description

Given two arrays A and B of size N. A[i] represents the time by which you can buy ith car without paying any money.

B[i] represents the profit you can earn by buying ith car. It takes 1 minute to buy a car so, you can only buy the ith car when the current time <= A[i] - 1.

Your task is to find maximum profit one can earn by buying cars considering that you can only buy one car at a time.

NOTE:

You can stary buying from time = 0.
Return you answer modulo 10^9 + 7.


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B[i] <= 10^9



Input Format
First argument is an integer array A represents the deadline of buying the cars.
Second argument is an integer array B represents the profit obtained after buying the cars.



Output Format
Return an integer denoting the maximum profit you can earn.



Example Input
Input 1:

 A = [1, 3, 2, 3, 3]
 B = [5, 6, 1, 3, 9]
Input 2:

 A = [3, 8, 7, 5]
 B = [3, 1, 7, 19]


Example Output
Output 1:

 20
Output 2:

 30


Example Explanation
Explanation 1:

 At time 0, buy car with profit 5.
 At time 1, buy car with profit 6.
 At time 2, buy car with profit 9.
 At time = 3 or after , you can't buy any car, as there is no car with deadline >= 4.
 So, total profit that one can earn is 20.
Explanation 2:

 At time 0, buy car with profit 3.
 At time 1, buy car with profit 1.
 At time 2, buy car with profit 7.
 At time 3, buy car with profit 19.
 We are able to buy all cars within their deadline. So, total profit that one can earn is 30.

"""


import heapq
from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        mod = 10**9+7
        max_profit = 0
        hashMap = defaultdict(list)
        
        for i in range(n):
            key = min(A[i]-1, n-1)
            hashMap[key].append(-B[i])
            
        heap = hashMap[n-1]
        heapq.heapify(heap)
        
        if len(heap) > 0:
            max_profit += -heapq.heappop(heap)
            
        for i in range(n-2, -1, -1):
            for val in hashMap[i]:
                heapq.heappush(heap, val)
                
            if len(heap) > 0:
                max_profit = (max_profit + (-heapq.heappop(heap))) % mod
                
        return max_profit
        
        
