class Solution:
    def maxSubArray(self, nums):
        current = best = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)

        return best