class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        nums=[]
        for i in s:
            nums.append(i)  
        k=len(s)    
        return k,nums   


c=Solution()

print(c.removeDuplicates([1,1,2]))