"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

"""


class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        result = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[left] ** 2 > nums[right] ** 2:
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result


solution = Solution()

assert solution.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert solution.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
