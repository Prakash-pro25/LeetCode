class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total=0
        while n!=0:
            total+=(n%10)**2
            n//=10
            if n==0 and total//10!=0:
                n=total
                total=0
        return total==1 

c=Solution()

print(c.isHappy(0))
print(c.isHappy(1))
print(c.isHappy(11))
print(c.isHappy(1111111))


