class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for i in jewels:
             count+=stones.count(i)

        return count     

c =Solution()

print(c.numJewelsInStones("aA","aaAAAtbes"))