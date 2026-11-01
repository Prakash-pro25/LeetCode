class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len("".join(set(s)))==len("".join(set(t)))


c=Solution()

print(c.isIsomorphic(s = "egg", t = "add"))
print(c.isIsomorphic(s = "f11", t = "b23"))
print(c.isIsomorphic(s = "paper", t = "title"))
