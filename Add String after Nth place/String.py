class Solution:
    def placeChar(self,S1,S2,N):
        for i in range(N,len(S1),N+len(S2)):
            S1= S1[:i]+S2+S1[i:]
        return S1
    
            
        

x=Solution()
print(x.placeChar("Quick Fox","*",2))
