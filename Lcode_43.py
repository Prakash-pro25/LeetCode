class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]

        i=len(num1)-1
        j=len(num2)-1
        a=0
        b=0

        while j>=0 or i>=0:
            if i>=0:
              a+=(ord(num1[i])-48)*(10**i) 
            if j>=0:
              b+=(ord(num2[j])-48)*(10**j) 
            i-=1
            j-=1

        ans=f"{a*b}"

        return ans
    

c=Solution()

print(c.multiply("123","1234"))
print(type(c.multiply("123","1234")))