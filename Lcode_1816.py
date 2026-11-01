class Solution(object):
    def truncateSentence(self, s, k):

        s=s.split()
        return " ".join(s[:k])
c=Solution()

print(c.truncateSentence("Hello how are you Contestant",4))