class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
               magazine=magazine.replace(i, "",1)
               result=True
            else:
                result=False
                break

        return result

c=Solution()

print(c.canConstruct("aa","aab"))