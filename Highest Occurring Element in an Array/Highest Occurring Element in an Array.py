class Solution:
    def mostFrequentElement(self, nums):
        freq={}
        count=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        max_freq=max(freq.values())
        for key,value in freq.items():
            if value==max_freq:
                return key
x=Solution()
print(x.mostFrequentElement([1, 2, 2, 3, 3, 3]))
