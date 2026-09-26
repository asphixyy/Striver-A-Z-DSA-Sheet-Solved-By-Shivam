class Solution:
    def frequencySort(self, s):
        dist = {}

        for ch in s:
            dist[ch] = dist.get(ch, 0) + 1

        ans = sorted(dist, key=lambda x: dist[x], reverse=True)

        result = ""
        for ch in ans:
            result += ch * dist[ch]

        return result

#OTHER APPROACH SIMPLER ONE
class Solution:
    def frequencySort(self, s):
        dist={}
        s=list(s)
        for i in range(len(s)):
            count=0
            for j in range(len(s)):
                if s[i] ==s[j]:
                    count+=1
            dist[s[i]]=count
        ans = sorted(dist, key=lambda item:(-dist[item],item))
        ans="".join(ans)
        
        result=""
        for i in ans:
            result+=i*dist[i]
        return result
