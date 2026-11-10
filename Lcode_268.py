class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        while m in nums:
            m+=1
        return m

c=Solution()

print(c.missingNumber([1,2,3,5]))