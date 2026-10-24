class Solution:
    def pattern7(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
                
            for k in range(2*i+1):
                print("*",end="")
            print()

x=Solution()
print(x.pattern7(4))
