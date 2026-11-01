class Solution(object):
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

c =Solution()

print(c.searchInsert([6,2,3,5],5))