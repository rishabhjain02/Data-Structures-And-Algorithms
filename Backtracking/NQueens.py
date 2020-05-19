"""

NQueens
Problem Description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. 

One solution to 8 Queen problem : https://imgur.com/LKQ3Q8S.png (Link)

Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

  


Problem Constraints
1 <= A <= 10


Input Format
First argument is an integer n denoting the size of chessboard


Output Format
Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.


Example Input
Input 1:
A = 4
 Input 2: 
A = 1
 


Example Output
Output 1:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
 Output 1: 
[
 [Q]
]
 


Example Explanation
Explanation 1:
There exist only two distinct solutions to the 4-queens puzzle:
 Explanation 1: 
There exist only one distinct solutions to the 1-queens puzzle:

"""

class Solution:
    # @param A : integer
    # @return a list of list of strings
    
    def NQueens(self, row, board, col_check, right_diagonal, left_diagonal, ans, N):
        if row >= N:
            temp = []
            for r in board:
                temp.append("".join(r))
            ans.append(temp)
            return
            
        for col in range(N):
            if col not in col_check and row+col not in right_diagonal and row-col not in left_diagonal:
                board[row][col] = "Q"
                col_check.add(col)
                left_diagonal.add(row-col)
                right_diagonal.add(row+col)
                
                self.NQueens(row+1, board, col_check, right_diagonal, left_diagonal, ans, N)
                
                board[row][col] = "."
                col_check.remove(col)
                left_diagonal.remove(row-col)
                right_diagonal.remove(row+col)
    
    def solveNQueens(self, A):
        d=" "
        if A == 1:
            return [["Q"]]
        board = [["." for j in range(A)] for i in range(A)]
        ans = []
        col_check = set()
        right_diagonal = set()
        left_diagonal = set()
        self.NQueens(0, board, col_check, right_diagonal, left_diagonal, ans, A)
        return ans
        
