class Solution(object):
    def longestConsecutive(self, nums):

        num_set = set(nums)
        longest = 0

        for i in num_set:
            if i - 1 not in num_set:
                count = 1

                while i + count in num_set:
                    count += 1

                longest = max(longest, count)

        return longest


c=Solution()

print(c.longestConsecutive([4,5,6,7,3,100,8]),end="\n\n")
print(c.longestConsecutive([100, 4, 200, 1, 3, 2]),end="\n\n")
print(c.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 1]),end="\n\n")
print(c.longestConsecutive([1, 2, 0, 1]),end="\n\n")
print(c.longestConsecutive([1, 0, -1]),end="\n\n")
print(c.longestConsecutive([1, 2, 3, 4]),end="\n\n")
print(c.longestConsecutive([5, 5, 5]),end="\n\n")
print(c.longestConsecutive([10, 20, 30]),end="\n\n")
print(c.longestConsecutive([2,3,4,6,7,8,9]))







