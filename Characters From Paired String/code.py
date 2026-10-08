def concat(N, string):
    ans = ""
    s = string.split()

    for i in range(0, int(N/2)):
        ans = s[i][:i+1] + s[-1-i][-1-i:]
        ans = ans + " "

    return ans

n=int(input())
l=input()
print(concat(n,l))
