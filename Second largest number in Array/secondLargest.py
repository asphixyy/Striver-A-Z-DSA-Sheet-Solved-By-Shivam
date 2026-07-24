class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(1+i,n):
                if nums[j]>nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
        #return nums
        for i in range(1,n):
             if nums[i] != nums[0]:
                return nums[i]
        return -1

x=Solution()
print(x.secondLargestElement( [8, 8, 8,8,8]))
