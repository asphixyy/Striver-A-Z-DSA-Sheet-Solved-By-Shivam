class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = count = 0

        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0

        return ans