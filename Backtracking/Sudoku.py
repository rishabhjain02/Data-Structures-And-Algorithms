"""

Sudoku
Problem Description
Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.  
A sudoku puzzle: (https://imgur.com/EK0XKBP.png)  and its solution numbers marked in red: (https://imgur.com/Jj8P4u5.png)      


Problem Constraints
1 <= N <= 9


Input Format
First argument is an array of array of characters representing the Sudoku puzzle.


Output Format
Modify the given input to the required answer.


Example Input
Input 1:
A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
     


Example Output
Output 1:
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
     


Example Explanation
Explanation 1:
Look at the diagrams given in the question.

"""

def find_empty(board):
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return (i, j)
    return None
    
def possible(board, num, row, col):
    n = len(board)
    m = len(board[0])
    
    for i in range(m):
        if board[row][i] == num:
            return False
                
    for i in range(n):
        if board[i][col] == num:
            return False
            
    box_x = (col // 3) * 3
    box_y = (row // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:
                return False
    
    
    return True

def solve(board):
    empty = find_empty(board)
    
    if not empty:
        return True
    else:
        row, col = empty
        
    for num in range(1,10):
        if possible(board, num, row, col):
            
            board[row][col] = num
            
            if solve(board):
                return True
            
            board[row][col] = 0
        
    return False
    
def find_ans(A):
    board = [[0 for i in range(9)] for j in range(9)]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != '.':
                board[i][j] = int(A[i][j])
  
    solve(board)
    return board

class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, A):
        board = find_ans(A)
        for i in range(9):
            temp = ""
            for j in range(9):
                temp += str(board[i][j])
            A[i] = temp
        
        
