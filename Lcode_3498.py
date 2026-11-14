class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i,v in enumerate(s):
            total+=(27 - (ord(v) - 96))*(i+1)
            
        return total

c=Solution()

print(c.reverseDegree("abc"))