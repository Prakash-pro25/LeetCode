class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)/2
        hp={}
        for i in nums:
          if i in hp:
            hp[i]+=1
          else:
            hp[i]=1

        for j in hp:
            if hp[j] > n:
                return j

c=Solution()

print(c.majorityElement([2,2,1,1,1,2,2]))
