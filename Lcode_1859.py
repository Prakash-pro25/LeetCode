class Solution(object):
    def sortSentence(self, s):

        s=s.split()
        a=[""]*len(s)
        for i in s:
            li=int(i[-1])-1
            a[li]=i[:-1:]
        return " ".join(a)

c =Solution()

print(c.sortSentence("is2 sentence4 This1 a3"))