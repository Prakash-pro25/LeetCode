class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True

        if not t:
            return False

        bf = -1

        for i in s:
            pos = t.find(i, bf + 1)

            if pos == -1:
                return False

            bf = pos

        return True
    
c=Solution()

print(c.isSubsequence(s = "abc", t = "ahbgdc"))
print(c.isSubsequence(s = "axc", t = "ahbgdc"))
print(c.isSubsequence(s = "a", t = "b"))
