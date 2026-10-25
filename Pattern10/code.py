class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
        for i in range(n-1):
            for j in range(n-1-i,0,-1):
                print("*",end="")
            print()

x=Solution()
print(x.pattern10(4))

            
