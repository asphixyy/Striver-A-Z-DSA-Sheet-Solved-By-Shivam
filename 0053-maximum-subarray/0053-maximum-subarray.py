class Solution:
    def maxSubArray(self, nums):
        current = best = nums[0]

        for num in nums[1:]:
            if current < 0:
                current = num
            else:
                current += num

            if current > best:
                best = current

        return best