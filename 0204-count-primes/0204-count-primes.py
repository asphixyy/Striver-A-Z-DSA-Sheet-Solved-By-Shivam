class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        i = 2

        while i * i < n:
            if prime[i]:
                prime[i * i:n:i] = [False] * (((n - 1 - i * i) // i) + 1)
            i += 1

        return sum(prime)