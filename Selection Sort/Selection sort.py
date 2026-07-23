class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            min_idx=i
            for j in range (i+1,n):
                if nums[j] < nums[min_num] :
                    min_idx=j
            nums[i],nums[min_idx]=nums[min_idx],nums[i]
        return nums
x=Solution()
print(x.selectionSort([7, 4, 1, 5, 3]))
