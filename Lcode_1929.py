class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums+nums

c=Solution()
print(c.getConcatenation([1,2,3]))
