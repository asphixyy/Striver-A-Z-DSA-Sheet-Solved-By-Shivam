class Solution:
    def sortZeroOneTwo(self, nums):
        for j in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i]>nums[(i+1)]:
                    nums[i],nums[(i+1)]=nums[(i+1)],nums[i] 
        return nums

x = Solution()
print(x.sortZeroOneTwo( [1, 0, 2, 1, 0]))
