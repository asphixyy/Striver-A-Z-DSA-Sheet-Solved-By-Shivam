class Solution:
    def reverseWords(self, s):
        string=s.split()
        string=string[::-1]
        return " ".join(string)

            
