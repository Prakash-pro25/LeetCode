class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        r=[]
        for i in s:
            r.append(i[::-1])
        return " ".join(r) 
    

c = Solution()

print(c.reverseWords("i am prakash"))