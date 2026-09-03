class Solution:
    def rotate(self, s, k):
        nums=list(s)  
       
        
        end=[]
        for i in range(k,len(nums)):
           end.append(nums[i])
        nums=nums[:k]
        end.extend(nums)
        return end
        
        
x=Solution()
print(x.rotate("HELLO",5))
        
        
