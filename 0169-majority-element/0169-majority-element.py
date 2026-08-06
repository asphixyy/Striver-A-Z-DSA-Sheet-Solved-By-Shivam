class Solution:
    def majorityElement(self, nums):
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for key in frequency:
            if frequency[key] > len(nums) // 2:
                return key


x = Solution()
print(x.majorityElement([3,3,4]))