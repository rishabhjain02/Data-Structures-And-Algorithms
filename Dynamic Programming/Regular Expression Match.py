"""

Regular Expression Match
Problem Description

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Problem Constraints
1 <= length(A), length(B) <= 10^4



Input Format
The first argument of input contains a string A.
The second argument of input contains a string B.



Output Format
Return 1 if the patterns match else return 0.



Example Input
Input 1:

 A = "aaa"
 B = "a*"
Input 2:

 A = "acz"
 B = "a?a"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Since '*' matches any sequence of characters. Last two 'a' in string A will be match by '*'.
 So, the pattern matches we return 1.
Explanation 2:

 '?' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0.


"""

# C++ Solution:

# int Solution::isMatch(const string A, const string B) {
#     int len_a = A.size();
#     int len_b = B.size();
    
#     bool match[len_a+1][len_b+1];
    
#     memset(match, 0, sizeof(match));
    
#     for(int i=0; i <= len_a; i++){
#         for(int j=0; j <= len_b; j++){
      
#             if (i==0 && j == 0)
#                 match[i][j] = 1;
      
#             else if (j==0)
#                 match[i][j] = 0;
                
#             else if (i==0){
#                 if (B[j-1] == '*')
#                     match[i][j] = match[i][j-1];
#             }
                
#             else if (B[j-1]=='*')
#                 match[i][j] = match[i-1][j] || match[i][j-1];
                
#             else if (A[i-1]==B[j-1] || B[j-1] == '?')
#                 match[i][j] = match[i-1][j-1];
#         }
#     }
    
#     return match[len_a][len_b];
# }



# Python Solution:

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        len_a = len(A)
        len_b = len(B)
        
        match = [[0 for j in range(len_b + 1)] for i in range(len_a + 1)]
        
        for i in range(len_a + 1):
            for j in range(len_b + 1):
                
                if i == 0 and j == 0:
                    match[i][j] = 1
                    
                elif j == 0:
                    match[i][j] = 0
                    
                elif i == 0:
                    match[i][j] = match[i][j-1] if B[j-1] == '*' else 0
                    
                elif B[j-1] == '*':
                    match[i][j] = match[i-1][j] or match[i][j-1]
                    
                elif A[i-1] == B[j-1] or B[j-1] == '?':
                    match[i][j] = match[i-1][j-1]
                    
        return match[-1][-1]
                    


