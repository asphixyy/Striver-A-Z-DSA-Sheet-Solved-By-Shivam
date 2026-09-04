class Solution:
    def largestOddNumber(self, num):
        if num[0]=="0":
           num= num[1:]
        for i in range(len(num),0,-1):
            if int(num[len(num)-1])%2==0:
                num=num[:-1]
        return (num)
        