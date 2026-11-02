class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a="abcdefghijklmnopqrstuvwxyz"

        for i in a:
            if (i in s and i not in t )or(i in t and i not in s):
                return i
            t=t.replace(i,"",1)
            s=s.replace(i,"",1)    


 