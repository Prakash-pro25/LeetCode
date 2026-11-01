class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        return s[k-1::-1]+s[k::]

c=Solution()

print(c.reverseStr(s = "abcdefg", k = 2))
print(c.reverseStr(s = "abcd", k = 2))

