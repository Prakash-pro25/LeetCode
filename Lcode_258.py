class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total=0
        while num!=0:
            total+=num%10
            num//=10
            if num==0 and total//10!=0:
                num=total
                total=0
        return total


c=Solution()

print(c.addDigits(29))