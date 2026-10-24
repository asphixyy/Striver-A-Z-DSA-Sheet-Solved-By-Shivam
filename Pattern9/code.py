class Solution:
    def pattern9(self, n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(2*i-1):
                print("*",end="")
            print()
        for i in range(n):
            for j in range(2*i-i):
                print(" ",end="")
            for k in range(2*n-2*i-1):
                print("*",end="")
            print()
x=Solution()
print(x.pattern9(4))
