
def bombHouses(N, X, A):
    ans = 0

    for i in range(N):
        if A[i] < X:
            ans = i + 1

    return ans


N, X = map(int, input().split())
A = list(map(int, input().split()))

print(bombHouses(N, X, A))
