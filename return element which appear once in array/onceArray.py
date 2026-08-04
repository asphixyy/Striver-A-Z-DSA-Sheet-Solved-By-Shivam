class Solution:
    def singleNumber(self, nums):
        for i in range (len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]==nums[i]:
                    count+=1
            if count==1:
                print(nums[i]) 
            else:
                pass
                


x = Solution()
print(x.singleNumber([5]))
