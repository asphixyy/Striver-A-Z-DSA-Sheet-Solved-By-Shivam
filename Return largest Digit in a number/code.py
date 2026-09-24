class Solution:
    def largestDigit(self, n):
        largest=0
        lst=list(str(n))
        for i in lst:
            if int(i)>largest:
                largest=int(i)
        return largest
