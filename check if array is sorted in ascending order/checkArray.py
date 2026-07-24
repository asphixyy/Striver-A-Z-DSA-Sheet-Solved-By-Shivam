class Solution:
    def isSorted(self, nums):
        n=len(nums)
        for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                return False
        return True

x=Solution()
print(x.isSorted([1, 2, 3, 4, 5]))
