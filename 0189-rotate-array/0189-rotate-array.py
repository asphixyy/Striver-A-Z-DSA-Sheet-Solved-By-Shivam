class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

**Other approach**
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        end=[]
        for i in range(k+1):
           end.append(nums[i])
        nums=nums[k+1:]
        nums.extend(end)
        return nums
x=Solution()
print(x.rotate( [1,2,3,4,5,6,7], 3))
