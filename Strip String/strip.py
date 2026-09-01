class Solution:
    def stripString(self,S1,K):
        result=""
        for i in range(len(S1)):
            if K==i:
                result=S1[i:len(S1)-K]
                return result
            
            
x=Solution()
print(x.stripString("abcdefghijk",3))
