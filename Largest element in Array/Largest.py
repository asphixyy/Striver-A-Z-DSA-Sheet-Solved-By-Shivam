class Solution:
    def largestElement(self, nums):
        n=len(nums)
        maxm=nums[0]
        for i in range(n):
            if nums[i]>maxm:
                maxm=nums[i]
        return maxm

        
x=Solution()
print(x.largestElement([7, -775, 1,4,7, 3]))
