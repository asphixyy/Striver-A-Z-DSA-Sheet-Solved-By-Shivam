class Solution:
    def moveZeroes(self, nums):
        zero=[]
        i=0
       
        while i <(len(nums)):
            if nums[i]==0:
                zero.append(nums[i])
                nums.pop(i)
            else:
                i+=1
        nums.extend(zero)
        return nums
               
x=Solution()
print(x.moveZeroes([0, 0, 0, 1, 3, -2]))
