class Solution:
    def countFrequencies(self, nums):
        frequency = {}

        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        result = []
        for key, value in frequency.items():
            result.append([key, value])

        return result
x=Solution()
print(x.countFrequencies([1,2,2,1,3]))
