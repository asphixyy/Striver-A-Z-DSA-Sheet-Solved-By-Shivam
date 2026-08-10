class Solution:
    def stockBuySell(self, arr):
        minm=arr[0]
        profit=0
        for i in range(1,len(arr)):
            minm=min(minm,arr[i])
            profit=max(profit,arr[i]-minm)
        return profit
