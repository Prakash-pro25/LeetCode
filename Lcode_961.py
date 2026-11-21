class Solution(object):
    def repeatedNTimes(self, nums):

        ht={}
        for i in nums:
            if i in ht:
                return i
            ht[i]=1


c=Solution()

print(c.repeatedNTimes([2,1,2,5,3,2]))

