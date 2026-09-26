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