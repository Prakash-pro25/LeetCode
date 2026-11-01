class Solution(object):
    def containsDuplicate(self, nums):
        return len(list(set(nums)))!=len(nums) 

c=Solution()

n=int(input())
nums=[int(input()) for i in range(n)]
print(c.containsDuplicate(nums))