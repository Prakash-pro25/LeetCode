class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i == i[::-1]:
                return i
        return ""

c=Solution()

print(c.firstPalindrome(["abc","car","ada","racecar","cool","Tenet","tenet"]))