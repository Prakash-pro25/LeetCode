class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        curr=0
        for num in nums:
            curr+=num
            arr.append(curr)

        return arr

c=Solution()  
print(c.runningSum([1,2,3,4]))       