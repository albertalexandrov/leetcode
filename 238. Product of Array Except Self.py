"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1 for _ in range(n)]

        #         adding prefix to output
        # [1, 1, 1, 1]
        # [1, 2, 3, 4]
        pre = 1
        for i in range(n):
            result[i] *= pre
            pre *= nums[i]
        print(result)
        post = 1
        for i in range(n - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        print(result)

        # как это работает не понятно ни хрена

        return result


s = Solution()

assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
