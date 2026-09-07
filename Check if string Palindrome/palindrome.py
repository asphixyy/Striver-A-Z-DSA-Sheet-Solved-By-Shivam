class Solution():
    def PalindromeString(self,s):
        reverse=s[::-1]
        if reverse==s:
            return True
        else:
            return False

x=Solution()
print(x.PalindromeString("pop"))
