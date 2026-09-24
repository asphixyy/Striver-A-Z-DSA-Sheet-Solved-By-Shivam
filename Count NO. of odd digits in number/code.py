class Solution:
    def countOddDigit(self, n):
        count=0
        lst=list(str(n))
        for i in lst:
            if int(i)%2!=0:
                count+=1
        return count
