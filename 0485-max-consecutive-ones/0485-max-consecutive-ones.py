class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > ans:
                    ans = count
            else:
                count = 0

        return ans

x = Solution()
print(x.findMaxConsecutiveOnes([1,1,0,1,1,1]))