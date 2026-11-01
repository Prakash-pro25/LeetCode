class Solution(object):
    def findDifference(self, nums1, nums2):
        un=list(set(nums1)&set(nums2))
        """ while un not in nums1 and un not in nums2: """
        print(nums1,nums2)     
        for i in un:
            nums1.remove(i)
            nums2.remove(i)


        return un,[nums1,nums2]


c=Solution()

print(c.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(c.findDifference(nums1 =[1,2,3,3],nums2 =[1,1,2,2]))
