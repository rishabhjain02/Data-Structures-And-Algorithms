"""

Compute nCr % p
Problem Description
Given three integers A, B and C, where A represents n, B represents r and C represents p and p is a prime number greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p. x! means factorial of x i.e. x! = 1 * 2 * 3... * x. NOTE: For this problem, we are considering 1 as a prime.     


Problem Constraints
1 <= A <= 10^6
1 <= B <= A
A <= C <= 10^9+7
    


Input Format
The first argument given is the integer A ( = n).
The second argument given is the integer B ( = r).
The third argument given is the integer C ( = p).


Output Format
Return the value of nCr % p.


Example Input
Input 1:
 A = 5
 B = 2
 C = 13
 Input 2:
 A = 6
 B = 2
 C = 13
     


Example Output
Output 1:
 10
Output 2:
 2
       


Example Explanation
Explanation 1:
 nCr( n=5 and r=2) = 10.
 p=13. Therefore, nCr%p = 10.

"""





"""
C ++ Solution:

long power(long x, long y, long p) 
{ 
    long res = 1;  
  
    while (y > 0) 
    { 
        if (y%2 == 1) 
            res = (res*x) % p; 
 
        y = y/2; 
        x = (x*x) % p; 
    } 
    return res; 
} 
 
long modInverse(long n, long p) 
{ 
    return power(n, p-2, p); 
} 
  
long find_ans(long n, long r, long p) 
{ 
   if (r==0) 
      return 1; 
  
    long fac[n+1]; 
    fac[0] = 1; 
    for (int i=1 ; i<=n; i++) 
        fac[i] = (fac[i-1]*i)%p; 
  
    return ((fac[n] * modInverse(fac[r], p) % p) % p * modInverse(fac[n-r], p) % p) % p; 
}
 
 
int Solution::solve(int A, int B, int C) {
    return find_ans(A,B,C); 
}



"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        def power(x, y, p): 
            res = 1  
            while (y > 0):
                if y%2 == 1: 
                    res = (res*x) % p
                y = y//2 
                x = (x*x) % p; 
            return res
            
        def modInverse(n, p):
            return power(n, p-2, p)
            
        def find_ans(n, r, p):
            if r == 0:
                return 1
                
            fac = [0]*(n+1)
            fac[0] = 1
            for i in range(1,n+1):
                fac[i] = (fac[i-1]*i)%p
                
            return ((fac[n] * modInverse(fac[r], p) % p) % p * modInverse(fac[n-r], p) % p) % p
            
        return find_ans(A, B, C)