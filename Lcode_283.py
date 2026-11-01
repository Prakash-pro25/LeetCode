class Solution(object):
    def moveZeroes(self, nums):
        iL = [i for i in nums if i != 0]
        iR = [i for i in nums if i == 0]
        nums[:] = iL + iR     
  


c=Solution()

nums=[0,1,0,3,12]
c.moveZeroes(nums)
print(nums)
