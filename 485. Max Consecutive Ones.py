"""
https://leetcode.com/problems/max-consecutive-ones/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation:
        The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3

Example 2:
    Input: nums = [1,0,1,1,0,1]
    Output: 2

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        consecutive = 0

        for num in nums:
            if num == 1:
                consecutive += 1
                res = max(res, consecutive)
            else:
                consecutive = 0

        return res


solution = Solution()

assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
