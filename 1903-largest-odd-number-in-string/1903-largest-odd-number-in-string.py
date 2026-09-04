class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]

        return ""

# OTHER APPROACH
class Solution:
    def largestOddNumber(self, num):
        if num[0]=="0":
           num= num[1:]
        for i in range(len(num),0,-1):
            if int(num[len(num)-1])%2==0:
                num=num[:-1]
        return (num)
        

x=Solution()
print(x.largestOddNumber("0214638"))
