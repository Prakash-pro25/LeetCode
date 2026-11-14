class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = "aeiou"
        v = 0
        c = 0
        for ch in set(s):
            if ch in vowels:
                v = max(v,s.count(ch))
            else:
                c = max(c,s.count(ch))
        return v + c
