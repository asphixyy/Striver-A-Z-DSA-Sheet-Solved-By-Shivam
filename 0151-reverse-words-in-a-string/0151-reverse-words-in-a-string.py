class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)


x = Solution()

print(x.reverseWords("welcome to the jungle"))
print(x.reverseWords(" amazing coding skills "))