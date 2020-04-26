"""

Lucky Numbers
A lucky number is a number which has exactly 2 distinct prime divisors. You are given a number N and you need to determine the count of lucky numbers between the range 1 to N (both inclusive). Input
The first argument contains one integer number N (1 ≤  N  ≤ 5000).
Output
Return an integer i.e the count of lucky numbers between 1 and N, both inclusive.
Examples Input
8
Output
1 
Explanation Testcase 1-
Between [1,8] there is only 1 lucky number i.e 6

"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        prime = [1]*(A+1)
	    spf = [x for x in range(A+1)]
        
        def SOE(n,prime,spf):
	        prime[0] = prime[1] = 0
	        for i in range(2,int(math.sqrt(n))+1):
	            if prime[i] == 1:
	                j=i
	                while(i*j<=n):
	                    prime[i*j] = 0
	                    if spf[i*j] == i*j:
	                        spf[i*j] = i
	                    j += 1
	    
	    
	    SOE(A,prime,spf)
	    
	    count = 0
	    
	    def isLucky(i):
	        s = set()
	        if spf[i] != i:
	            while(i>1):
	                s.add(spf[i])
	                i = i//spf[i]
	                if len(s)>2:
	                    break
	        return len(s)==2
	        
	    for i in range(6,A+1):
	        if isLucky(i):
	            count+=1
	        
	    return count
        
