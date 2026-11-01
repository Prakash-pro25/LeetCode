class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        
        return "".join(word1)=="".join(word2)


c=Solution()

print(c.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))
print(c.arrayStringsAreEqual(["a", "cb"],["ab", "c"]))
print(c.arrayStringsAreEqual( ["abc", "d", "defg"],["abcddefg"]))
