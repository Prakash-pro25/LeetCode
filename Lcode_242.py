class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        clean_str1 = s.replace(" ", "").lower()
        clean_str2 = t.replace(" ", "").lower()

        str1="".join(sorted(clean_str1))
        str2="".join(sorted(clean_str2))


        return str1==str2