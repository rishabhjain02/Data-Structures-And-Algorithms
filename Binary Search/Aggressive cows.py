"""

Aggressive cows
Problem Description
Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows. His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?   


Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 10^9
2 <= B <= N


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the largest minimum distance possible among the cows.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 3
  Input 2:      
A = [1, 2]
B = 2
    


Example Output
Output 1:
 2
  Output 2:      
 1
    


Example Explanation
Explanation 1:
 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
  Explanation 2:      
 
The minimum distance will be 1.

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, stall, cows):
        n = len(stall)
        stall.sort()
        def isPossible(k,cows):
            last_pos = stall[0]
            cows_placed = 1
            for i in range(1,n):
                if stall[i]-last_pos >= k:
                    cows_placed += 1
                    last_pos = stall[i]
            return cows_placed>=cows
            
        low = 1
        high = stall[n-1]-stall[0]
        ans = 0
        while(low<=high):
            mid=low+(high-low)//2
            if isPossible(mid,cows):
                ans=mid
                low=mid+1
            else:
                high=mid-1
            
        return ans
            
