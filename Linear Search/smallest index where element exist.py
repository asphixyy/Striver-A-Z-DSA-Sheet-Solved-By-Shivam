class Solution:
    def linearSearch(self, nums, target):
        for i in nums:
            if target in nums:
                return i-1
        else:
            return -1
               
x=Solution()
print(x.linearSearch([2, 3, 4, 5, 3],5))
