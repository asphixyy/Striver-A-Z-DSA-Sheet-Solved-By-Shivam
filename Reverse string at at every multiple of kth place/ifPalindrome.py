class Solution:
    def palindrome(self, s1,s2,k):
        new=""
        othernew=""
        
        n, m = len(s1), len(s2)
      #  k1 = k//n
        
        new=s1[-k:]+s1[:-k]
      #  k2 = k//m
        
        othernew=s2[k:]+s2[:k]
        s3=new+othernew
        #print(new)
        #print(othernew)
        
        #s3=s1[k:]+s1[:k]+s2[k+1]+s2[:k+1]
        
        if s3==s1+s2:
            return True,s3
        else:
            return False,s3
        return new,othernew
            
        
        
x=Solution()
print(x.palindrome("abcde","abcd",3))
