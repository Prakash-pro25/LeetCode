class Solution(object):
    def reverseVowels(self, s):

        vol="AEIOUaeiou"
        symbols = [(i, char) for i, char in enumerate(s) if char not in vol]
        str1=""
        for i in s:
            if i in vol:
                str1+=i

        str1=list(str1[::-1])      
        for sy in symbols:
            x,y=sy
            str1.insert(x,y)
            

        return "".join(str1)


c=Solution()

print(c.reverseVowels("IceCreAm"))