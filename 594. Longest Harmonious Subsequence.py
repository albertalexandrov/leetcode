"""
https://leetcode.com/problems/longest-harmonious-subsequence/

We define a harmonious array as an array where the difference between its maximum value and
its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among
all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or
no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
    Input: nums = [1,2,3,4]
    Output: 2

Example 3:
    Input: nums = [1,1,1,1]
    Output: 0

"""

from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        counter = Counter(nums)
        longest = 0
        for num, freq in counter.items():
            if num + 1 in counter:
                longest = max(longest, freq + counter[num + 1])
        return longest


solution = Solution()
assert solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
assert solution.findLHS([1, 2, 3, 4]) == 2
assert solution.findLHS([1, 1, 1, 1]) == 0
