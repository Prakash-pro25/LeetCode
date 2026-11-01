class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.replace("-","").lower()
        s=list(s)
        
        for i in range(len(s),0,-4):
            s.insert(i,"-")

        return "".join(s).strip("-")

c=Solution()

print(c.licenseKeyFormatting("rh-gh-fje-kfj",4))
            

