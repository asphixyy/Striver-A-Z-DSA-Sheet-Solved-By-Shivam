class Solution:
    def pattern5(self, n):
        for i in range(1,n+1):
            for j in range(n+1-i):
                print("*",end="")
            print()
        return

x=Solution()
print(x.pattern5(4))
