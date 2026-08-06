class Solution:
    def longestSubarray(self, nums, k):
        longest = 0

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]

                if total == k:
                    longest = max(longest, j - i + 1)

        return longest


x = Solution()
print(x.longestSubarray([10,5,2,7,1,9], 15))
