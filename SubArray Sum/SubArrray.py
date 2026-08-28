class Solution:
    def subarraySum(self, nums, k):
        sums=0
        count=0
        for i in range(len(nums)):
            sums=0
            for j in range(i,len(nums)):

                if j<len(nums):
                    sums+=nums[j]
                if sums==k:
                    count+=1
        return count
                

x=Solution()
print(x.subarraySum(  [1,2,3],  3))
