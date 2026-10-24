class Solution:
    def pattern8(self, n):
        for i in range(1,n+1):
            for j in range(i-1):
                print(" ",end="")
            for k in range(2*n-2*i+1):
                print("*",end="")
            print()
x=Solution()
print(x.pattern8(2))
