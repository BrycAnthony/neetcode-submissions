class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        ana_s, ana_t = {}, {}

        for i in s:
            if i in ana_s:
                ana_s[i] = ana_s[i] + 1
            else:
                ana_s[i] = 1
        for i in t:
            if i in ana_t:
                ana_t[i] = ana_t[i] + 1
            else:
                ana_t[i] = 1

        return ana_s == ana_t