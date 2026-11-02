class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        for v in s:
            count[v] = count.get(v, 0) + 1

        for i, v in enumerate(s):
            if count[v] == 1:
                return i

        return -1

c=Solution()

print(c.firstUniqChar("leetcode"))