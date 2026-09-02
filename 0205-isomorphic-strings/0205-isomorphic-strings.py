class Solution:
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            # Check s -> t
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False
            else:
                s_to_t[s[i]] = t[i]

            # Check t -> s
            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]:
                    return False
            else:
                t_to_s[t[i]] = s[i]

        return True