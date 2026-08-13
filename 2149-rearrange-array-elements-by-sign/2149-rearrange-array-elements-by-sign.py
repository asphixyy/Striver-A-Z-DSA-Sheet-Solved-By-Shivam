class Solution:
    def rearrangeArray(self, nums):
        positive=[]
        negative=[]
        answer=[]
        for i in range(len(nums)):
            if nums[i]<0:
                negative.append(nums[i])
            else:
                positive.append(nums[i])
        for i in range(len(positive)):
            answer.append(positive[i])
            answer.append(negative[i])

        return answer