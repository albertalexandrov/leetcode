"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

"""


class Solution(object):
    """
    Time: O(n)
    Space: O(1)

    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for num in nums:
            result ^= num

        return result


solution = Solution()

assert solution.singleNumber([2, 2, 1]) == 1
assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
assert solution.singleNumber([1]) == 1
