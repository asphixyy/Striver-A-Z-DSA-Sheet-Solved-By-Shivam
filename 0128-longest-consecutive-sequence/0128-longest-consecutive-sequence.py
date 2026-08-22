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
        
        
x=Solution()
print(x.longestConsecutive( [100, 4, 200, 1, 3, 2]))