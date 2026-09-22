class Solution():
    def primeNo(self,start,end):
        real_count=0
        for i in range(start,end+1):
            j=1
            
            count=0
            while j<=i:
                if i%j==0:
                    count+=1
                j+=1
            if count==2:
                print("Prime",i)
                total=0
                temp=i
                while temp > 0:
                    total += temp % 10     
                    temp //= 10  
              #  print("total",total%2)
                if (total%2)==0:
                    real_count= real_count + 1
               # print(real_count)
        return real_count
        
x=Solution()

print(x.primeNo(10,20))
