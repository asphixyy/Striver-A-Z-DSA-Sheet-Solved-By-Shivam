class Solution:
    def countDigitOccurrences(self, nums, digit):
        count = 0
        digit = str(digit)

        for num in nums:
            for ch in str(num):
                if ch == digit:
                    count += 1

        return count