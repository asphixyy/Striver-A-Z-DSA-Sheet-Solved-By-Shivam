class Solution:
    def countFrequencies(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=[]
        for key in freq:
            result.append([key,freq[key]])
        return result
x=Solution()
print(x.countFrequencies([1, 2, 2, 1, 3])
