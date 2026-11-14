class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        c,v=0,0

        for i in s:
            if i in "aeiou":
                v+=1
            elif i in "bcdfghjklmnpqrstvwxyz":
                c+=1
        
        return v//c if c !=0 else 0