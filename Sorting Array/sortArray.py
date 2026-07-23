class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums

x=Solution()
print(x.bubbleSort([7, 4, 1, 5, 3]))
