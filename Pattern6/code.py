class Solution:
    def pattern6(self, n):
        for i in range(1,n+1):
            for j in range(1,n+2-i):
                print(j,end="")
            print()
        return

x=Solution()
print(x.pattern6(4))
