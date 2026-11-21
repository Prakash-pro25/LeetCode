class Solution(object):
    def numIdenticalPairs(self, nums):
        ht = {}
        total = 0

        for i in nums:
            if i in ht:
                total += ht[i]
                ht[i] += 1
            else:
                ht[i] = 1

        return total

c =Solution()

print(c.numIdenticalPairs([1,2,3,1,1,3]))