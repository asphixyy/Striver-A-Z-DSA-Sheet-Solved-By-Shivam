class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(i,end="")
            print()
        return

x=Solution()
print(x.pattern4(4))
