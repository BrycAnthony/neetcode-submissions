class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        ana_t = {}

        for char in s:
            if char in ana:
                ana[char] = ana[char] + 1
            else:
                ana[char] = 1
        for char in t:
            if char in ana_t:
                ana_t[char] = ana_t[char] + 1
            else:
                ana_t[char] = 1
        if ana == ana_t:
            return True
        else:
            return False