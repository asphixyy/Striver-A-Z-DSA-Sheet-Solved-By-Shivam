class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = bytearray(b'\x01') * n
        prime[0] = prime[1] = 0

        i = 2

        while i * i < n:
            if prime[i]:
                start = i * i
                count = (n - 1 - start) // i + 1
                prime[start:n:i] = b'\x00' * count

            i += 1

        return sum(prime)