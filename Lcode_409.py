class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht={}
        for i in s:
            if i in ht:
                ht[i]+=1
            else:
                ht[i]=1
        odd=False
        pali=0
        for i in ht:
            if ht[i]%2 !=0:
                odd=True
                pali+=ht[i]-1
            else:
                pali+=ht[i]


        return pali+1 if odd else pali
    

c=Solution()

print(c.longestPalindrome("abccccdd"))