"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers
in the range [1, n] that do not appear in nums.

Example 1:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

Example 2:
    Input: nums = [1,1]
    Output: [2]

"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]


solution = Solution()
assert solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
