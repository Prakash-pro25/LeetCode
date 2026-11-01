class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        prefix = 1

        # Left product
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Right product
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

            




c=Solution()

print(c.productExceptSelf([1,2,3,5,0,0]))

