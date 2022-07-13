"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

"""
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [item[0] for item in Counter(nums).most_common(k)]


s = Solution()

assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert s.topKFrequent([1], 1) == [1]
