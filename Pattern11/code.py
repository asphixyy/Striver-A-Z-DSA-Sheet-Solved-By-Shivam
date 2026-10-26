class Solution:
    def pattern11(self, n):
        for i in range(0,n):
            if i%2 == 0:
                temp = 1
            else:
                temp = 0
            for j in range(0,i+1):
                if(j < i):
                    print(temp, end = " ")
                else:
                    print(temp, end = " ")
                if temp == 1:
                    temp = 0
                else:
                    temp = 1
            print()
x=Solution()
x.pattern11(6)
