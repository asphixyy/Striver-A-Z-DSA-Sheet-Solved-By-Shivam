class Solution:
    def checkPerfectNumber(self, n):
        if n <= 1:
            return False

        sums = 1

        i = 2
        while i * i <= n:
            if n % i == 0:
                sums += i

                if i != n // i:
                    sums += n // i

            i += 1

        return sums == n