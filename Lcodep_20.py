class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par={"{":0,"}":0,"[":0,"]":0,"(":0,")":0}
        for i in s:
            par[i]=s.count(i)
        if par["{"]==par["}"] and par["("]==par[")"] and par["["]==par["]"]:
           return True  
        else:
            return False

c=Solution()

print(c.isValid("([)]"))
