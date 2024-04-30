import collections


class Solution(object):
    def numIdenticalPairs(self, nums):
        repeat = collections.defaultdict(int)
        num = 0
        for v in nums:
            num += repeat[v]
            repeat[v] += 1
        return num


solution = Solution()
solution.numIdenticalPairs([1, 1, 1, 1])
