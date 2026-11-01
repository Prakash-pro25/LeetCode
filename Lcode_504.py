class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return "0"
        b='-' if num<0 else ""
        num=abs(num)
        a=""
        while num:
            a+=str(num%7)
            num//=7

        return b+a[::-1]
        

c=Solution()

print(c.convertToBase7(-10))