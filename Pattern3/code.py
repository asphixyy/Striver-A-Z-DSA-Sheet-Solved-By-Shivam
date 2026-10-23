class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(j+1,end="")
            print()
        return

x=Solution()
print(x.pattern3(4))
