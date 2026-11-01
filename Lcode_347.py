class Solution(object):
    def topKFrequent(self, nums, k):
        arr = []

        for i in nums:
            if i not in arr:
                arr.append(i)

        arr.sort(key=nums.count, reverse=True)

        return arr[:k]


c = Solution()
print(c.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))



