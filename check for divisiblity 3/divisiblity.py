class Solution():
    def Divisible3(self,start,end):
        count=0
        sums=0
        for i in range(start,end):
            sums=0
            j=i
            while j>0:
                sums=sums+j%10
                j=j//10
            if i%3==0 and sums%2==0:
                count+=1
        return count
        
x=Solution()
print(x.Divisible3(1,100))
