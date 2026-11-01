class Solution(object):
    def restoreString(self, s, indices):
        ans=[""]*len(s)
        for i in range(len(s)):
            ans[indices[i]]=s[i]
        return "".join(ans)

c = Solution()

print(c.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))