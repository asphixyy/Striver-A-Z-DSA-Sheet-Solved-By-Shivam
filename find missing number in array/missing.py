class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        i = 0

        while i <= n:
            if i in nums:
                i += 1
            else:
                return i

x = Solution()
print(x.missingNumber([0, 2, 3, 1, 4]))
