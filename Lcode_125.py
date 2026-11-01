class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        str1=""
        i=0
        while i<len(s):
            if s[i].isalnum():
                str1+=s[i]
            i+=1   
        return str1==str1[::-1]

    def isPalindrome1(self,s):
        s=s.lower()
        sy=""" ,@:.&*#$%"!?_-+=/|{[]}():;><^`\~'"""
        for i in sy:
            s=s.replace(i,'')
        return s==s[::-1] 
         

c=Solution()    

print(c.isPalindrome1("A man, a plan, a canal: Panama"))
print(c.isPalindrome1(" "))
print(c.isPalindrome1("race a car"))
print(c.isPalindrome1("0p"))



