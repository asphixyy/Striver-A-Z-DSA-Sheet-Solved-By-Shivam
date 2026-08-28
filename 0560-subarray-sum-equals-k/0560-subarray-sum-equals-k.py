class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        hashmap = {0: 1}

        for num in nums:
            sums += num

            if sums - k in hashmap:
                count += hashmap[sums - k]

            hashmap[sums] = hashmap.get(sums, 0) + 1

        return count