class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest = 0
        for i in nums_set:

            if i - 1 not in nums_set:
                count = 1

                while i + count in nums_set:
                    count += 1

                longest = max(longest, count)

        return longest
