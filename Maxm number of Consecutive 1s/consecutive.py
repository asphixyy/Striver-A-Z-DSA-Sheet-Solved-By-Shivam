class Solution:
    def findMaxConsecutiveOnes(self, nums):
        i=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1 and nums[i+1]!=0:
                count+=1
        return count

x = Solution()
print(x.findMaxConsecutiveOnes( [1, 1, 0, 0, 1, 1, 1, 0]))
