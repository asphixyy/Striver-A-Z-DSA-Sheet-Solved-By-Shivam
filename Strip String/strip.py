class Solution:
    def stripString(self,S1,K):
        for i in range(len(S1)):
            if K==i:
                return S1[K:]
            
            
x=Solution()
print(x.stripString("abcdefghijk",3))
