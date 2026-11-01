class Solution(object):
    def halvesAreAlike(self, s):
        vol="aeiouAEIOU"
        mid=(len(s)//2)
        a=s[:mid]
        b=s[mid:]
        ca=0
        cb=0
        for i in range(len(a)):
            if a[i] in vol:
                ca+=1
            if b[i] in vol:
                cb+=1
        return  cb==ca

c =Solution()

print(c.halvesAreAlike("book"))