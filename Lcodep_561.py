class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=list({(i,j) if i>j else(j,i) for i in nums for j in nums if j!=i})
        m1=[]
        for i in range(len(m)):
            if i<len(m)-1:
             c1=m[i]+m[i+1]
            if sum(c1) == sum(nums):
                m1.append(c1)


        return m1,m

c=Solution()

a,b=c.arrayPairSum([1,2,3,4])
print(a)
print(b)