class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        symbols = [(i, char) for i, char in enumerate(s) if not char.isalpha()]
        str1=""
        for i in s:
            if i.isalpha():
                str1+=i

        str1=list(str1[::-1])      
        for sy in symbols:
            x,y=sy
            str1.insert(x,y)
            

        return "".join(str1),symbols

c=Solution()
print(c.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(c.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
