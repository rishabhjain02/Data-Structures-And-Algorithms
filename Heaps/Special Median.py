"""

Special Median
Problem Description

You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
Median is the middle element in the sorted list of elements. If the number of elements are even then median will be (sum of both middle elements)/2.

Return 1 if the array is special else return 0.

NOTE:

For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]


Problem Constraints
1 <= N <= 1000000.
A[i] is in the range of a signed 32-bit integer.



Input Format
First and only argument is an integer array A.



Output Format
Return 1 if the given array is special else return 0.



Example Input
Input 1:

 A = [4, 6, 8, 4]
Input 2:

 A = [2, 7, 3, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explantion 1:

 Here, 6 is equal to the median of [8, 4].
Explanation 2:

 No element satisfies any condition.

"""


import heapq

# Function to add number to lower or higher heap
def addToHeap(num, lower, higher):
    if len(lower) == 0 or num < -lower[0]:
        heapq.heappush(lower, -num)
    else:
        heapq.heappush(higher, num)
        
# Function to balance the heaps if heaps become unbalanced
# heaps will be unbalanced if difference of their lengths is more than 1
def balance(lower, higher):
    if len(lower) - len(higher) >= 2:
        heapq.heappush(higher, -heapq.heappop(lower))
        
    if len(higher) - len(lower) >= 2:
        heapq.heappush(lower, -heapq.heappop(higher))
        
# Function to find median from the heaps        
def findMedian(lower, higher):
    if len(lower) == len(higher):
        return (-lower[0] + higher[0])/2
    else:
        if len(lower) > len(higher):
            return -lower[0]
        else:
            return higher[0]
    
# Function to check for the first property mentioned in question 
def check_left(A):
    lower = []
    higher = []
    median = 0
    for i in range(len(A)-1):
        num = A[i]
        addToHeap(num, lower, higher)
        balance(lower, higher)
        median = findMedian(lower, higher)
        if median == A[i+1]:
            return 1
    return 0
    
# Function to check for the second property mentioned in question    
def check_right(A):
    lower = []
    higher = []
    median = 0
    for i in range(len(A)-1, 0, -1):
        num = A[i]
        addToHeap(num, lower, higher)
        balance(lower, higher)
        median = findMedian(lower, higher)
        if median == A[i-1]:
            return 1
    return 0

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return check_left(A) or check_right(A)
        
        
        