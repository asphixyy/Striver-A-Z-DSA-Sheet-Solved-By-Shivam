def jumpingNumber(X):
    for i in range(0, 10):
        print(i, end=" ")

    for i in range(10, X+1):
        s = str(i)

        for j in range(len(s)-1):
            if abs(int(s[j]) - int(s[j+1])) != 1:
                break
        else:
            print(i, end=" ")

X = int(input())
jumpingNumber(X)
