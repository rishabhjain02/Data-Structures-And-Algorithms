"""

Finish Maximum Jobs
Problem Description

There are N jobs to be done but you can do only one job at a time.

Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.

Your aim is to select jobs in such a way so that you can finish maximum number of jobs. Return the maximum number of jobs you can finish.



Problem Constraints
1 <= N <= 10^5

1 <= A[i] < B[i] <= 10^9



Input Format
First argument is an integer array A of size N denoting the start time of the jobs.
Second argument is an integer array B of size N denoting the finish time of the jobs.



Output Format
Return an integer denoting the maximum number of jobs you can finish.



Example Input
Input 1:

 A = [1, 5, 7, 1]
 B = [7, 8, 8, 8]
Input 2:

 A = [3, 2, 6]
 B = [9, 8, 9]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 We can finish the job in the period of time: (1, 7) and (7, 8).
Explanation 2:

 Since all three jobs collide with each other. We can do only 1 job.

"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        jobs = 0
        
        pairs = sorted(zip(A, B), key = lambda x: x[1])
        
        jobs = 1
        last_end = pairs[0][1]
        
        for i in range(1, n):
            if pairs[i][0] >= last_end:
                jobs += 1
                last_end = pairs[i][1]
        
        return jobs
