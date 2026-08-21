class Solution:
    def leaders(self, nums):
        leader=[]
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                leader.append(nums[i-1])
        leader.append(nums[-1])   
        return leader

x=Solution()
print(x.leaders([1, 2, 5, 3, 1, 2]))
