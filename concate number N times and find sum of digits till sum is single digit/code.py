class Solution():
    def Divisible3(self,N,K):
        sums=""
        for i in range(K):
            sums=sums+N
        
        sums=int(sums)
        real_sum=0
        
        while sums>0:
            real_sum+=sums%10
            sums=sums//10
            real_sum=int(real_sum)
            
        while real_sum>9:
            sums=real_sum
            real_sum=0
            while sums>0:
                real_sum+=sums%10
                sums=sums//10
    
        return int(real_sum)
        
x=Solution()
print(x.Divisible3("9875",4))
