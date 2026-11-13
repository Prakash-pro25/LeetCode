class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        ht={}
        result=False
        for i in range(len(s)):

            if pattern[i] in ht:
                if ht[pattern[i]] == s[i]:
                    result=True
                else:
                    result=False
                    break
            else:
                ht[pattern[i]]=s[i]
        return result
        

               



