class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
            
x=Solution()
print(x.singleNumber([4,1,2,1,2]))