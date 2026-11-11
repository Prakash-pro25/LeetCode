class Solution(object):
    def missingNumber(self, nums):
        nums_set=set(nums)
        n=0
        while n in nums_set:
            n+=1
        return n
    
c=Solution()

print(c.missingNumber([1]))