def Count(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 3 == 0:
            j = i
            sums = 0
            while j > 0:
                sums += j % 10
                j = j // 10
            if sums % 2 == 0:
                count += 1
    return count

start = int(input())
end = int(input())
print(Count(start, end))
