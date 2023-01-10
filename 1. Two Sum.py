"""
https://leetcode.com/problems/two-sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

"""


class Solution1:
    """Решение 1.

    Time: О(n)
    Space: O(n)

    Предпочтительное решение благодаря скорости

    """
    def two_sum(self, nums, target):
        lookups = {}  # содержит пары элемент-индекс

        for idx, num in enumerate(nums):
            if target - num in lookups:
                return lookups[target - num], idx
            else:
                lookups[num] = idx


solution1 = Solution1()

assert solution1.two_sum([2, 7, 11, 15], 9) == (0, 1)


class Solution2:
    """Решение 2.

    Time: О(n^2)
    Space: O(1)

    Решение неоптимальное из-за скорости

    """

    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


solution2 = Solution2()

assert solution2.two_sum([2, 15, 11, 7], 9) == (0, 3)
