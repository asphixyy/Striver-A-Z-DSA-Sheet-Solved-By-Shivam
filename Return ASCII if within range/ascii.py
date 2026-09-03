class Solution:  
    def AsciiValue(self, s,N,M):
        count=0
        for i in s:
            if ord(i) in range(N,M+1):
                count+=1
        return count
        
        
x=Solution()
print(x.AsciiValue("AB*abXYDEF#@pqr",67,75))
        
        
