def majority(N, arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > N // 2:
            return num
    return "No Majority Element"


N = int(input())
arr = list(map(int, input().split()))
print(majority(N, arr))
