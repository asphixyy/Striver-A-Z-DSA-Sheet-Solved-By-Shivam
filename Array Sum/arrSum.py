class Solution():
    def Sums(self,nums,k):
        sumArr=[]
        for j in range(len(nums)):
            for i in range(1,len(nums)):
                if nums[j]+nums[i]==k:
                    sumArr.append([nums[j],nums[i]])
        return sumArr
        
x=Solution()
print(x.Sums([8,-1,3,4,-3,2,1],5))
