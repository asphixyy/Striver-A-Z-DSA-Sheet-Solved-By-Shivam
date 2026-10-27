def countPrimes(A, B):
    prime = []
    for i in range(A, B+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            temp = i
            sums = 0
            while temp > 0:
                sums = sums + temp % 10
                temp = temp // 10

            if sums % 2 == 0:
                prime.append(i)

    x = list(set(prime))

    return len(x)

A = int(input())
B = int(input())
print(countPrimes(A, B))
