class Solution:
    def LCM(self, n1, n2):
        i = 1

        while True:
            check=n1*i
            if check%n2==0:
                return check
            i+=1

x = Solution()
print(x.LCM(4, 6))
